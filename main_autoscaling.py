# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:22:09 2020

__author__ = 'Inger Annett Grünbeck'
__email__ = 'inger.gruenbeck@gmail.com'
"""


import nibabel as nib
import numpy as np
import os
from copy import deepcopy
from scipy.stats import zscore
from skimage import img_as_ubyte
from skimage.exposure import rescale_intensity
from datetime import datetime



def import_data(img_path, affine_header = True):
    """
    Importing nifti images
    
    :param img_path: path to folder containing nifti images
    :param affine_header: Whether to store the affine transformation and the 
        header of the images
    
    :return: list of 3D images. List of affine transformations and headers 
        are returned if affine_header is true 
    """    
    
    image_list = []
    if affine_header:
        image_affine = []
        image_header = []
    

    for dirname, _, filenames in os.walk(img_path):
        for file in sorted(filenames):
            img = nib.load(os.path.join(dirname, file))
            image = img.get_fdata()
            image_swap = np.transpose(image)
            image_list.append(image_swap)
            if affine_header:
                image_affine.append(img.affine)
                image_header.append(img.header)
        
    if affine_header:
        return image_list, image_affine, image_header
    else:
        return image_list

def dimension_3to1(image_list):
    """
    Tranfsorming list of 3D images to 1D
    
    :param image_list: List of 3D images
    :return: List of 1D images
    """
    
    D1_image = []
    shape = image_list[0].shape
    dim = shape[0]*shape[1]*shape[2]
    
    for element in image_list:
        D1_image.append(np.reshape(element, (dim,1)))
        
    return D1_image

def dimension_1to3(image_list):
    """
    Tranfsorming list of 1D images to 3D with shape (120, 256, 256)
    
    :param image_list: List of 1D images
    :return: List of 3D images
    """
    
    D3_image = []
    
    for element in image_list:
        D3_image.append(np.reshape(element, (120, 256, 256)))
        
    return D3_image

def create_segment(D1_image, D1_mask):
    """
    Creating a list of segments based on a list og 1D images and a list of 
    1D binary masks
    
    :param D1_image: List of 1D images
    :param 1D1_mask: List of 1D binary masks
    
    :return: List of 1D segments
    """
    
    segment = []
    volume = 0
    
    for element in D1_image:
        val_ind = 0
        segment.append(np.zeros(0))
        
        for value in element:
            if D1_mask[volume][val_ind] == 1:
             
                segment[volume] = np.append(segment[volume], value)
            
            val_ind += 1
            
        volume += 1
    
    return segment

def zscore_calc(segment_list):
    """
    Calculating the z-score of elements in a list
    
    :param segment_list: List of 1D segments

    :return: the normalised input list
    """
    
    segment_z = []
    for ind in range(len(segment_list)):
        segment_z.append(zscore(segment_list[ind]))
        
    return segment_z

def threshold(D1_mask, segment):
    """
    Defining new binary masks. Voxels with z-score outside of range [-3,3] are
    changed to 0 in new binary masks
    
    :parma D1_mask: List of binary masks
    :param segment: List of segments containing normalised values as z-scores
    
    :return: List of new binary masks for segments
    """
    
    new_mask = []
    
    for ind in range(len(D1_mask)):
        new_mask.append(np.ones(int(D1_mask[ind].sum())))
    
    for element in range(len(segment)):
        for ind in range(len(segment[element])):
            if segment[element][ind] <-3:
                new_mask[element][ind] = 0
            elif segment[element][ind] > 3:
                new_mask[element][ind] = 0
                
    return new_mask

def create_full_mask(new_mask, original_mask):
    """
    Creating full, new binary masks based on the new masks of the segments
    
    :param new_mask: List of binary masks of segments
    :param original_mask: List of the original masks of the imported images
    
    :return: List of the new, full masks
    """
    
    full_mask = deepcopy(original_mask)
    mask_copy = deepcopy(new_mask)
    
    for ind in range(len(original_mask)):
        for value in range(len(original_mask[ind])):    
            if original_mask[ind][value] == 1:
                full_mask[ind][value] = mask_copy[ind][0]
                mask_copy[ind] = np.delete(mask_copy[ind],[0])

    return full_mask

def saving(D3_list, affine_list, header_list, path):
    """
    Saving 3D images.
    
    :param 3D_list: List of 3D images
    :param affine_list: List of affine transformations
    :param header_list: List of headers
    :param path: List of paths to save-folder
    """
    
    for index in range(len(D3_list)):
        transposed = np.transpose(D3_list[index])
        temp_seg = nib.Nifti1Image(transposed, affine_list[index], header_list[index])
        
        if index < 10:
            name = path+'/00'+str(index)+'_seg.nii'
        elif index >= 10 and index < 100:
            name = path + '/0'+str(index)+'_seg.nii'

        nib.save(temp_seg, name)

def minimum(D1_image):
    """
    Detecting the minimium value in a list
    
    :param D1_image: List of 1D images
    
    :return: The minimum
    """
    
    min_seg = []

    for element in D1_image:
        min_seg.append(element.min())
        
    global_min = 0
    for element in min_seg:
        if element<= global_min:
            global_min = element
            
    return global_min

def adjust_zscore(D1_zscore, global_min):
    """ 
    Adding the global minimun to the normalised images
    
    :param D1_zscore: List of normalised 1D images
    :param global_minimum: The global minimum
    
    :return: List of shifted, normalised 1D images
    """
    
    seg_adjusted = []
    for ind in range(len(D1_zscore)):
        seg_adjusted.append(D1_zscore[ind] - global_min)
        
    return seg_adjusted

def z_to_8bits(zscore_list):
    """
    Rescaling the normalised intensity values of 1D images to 1D 8-bit images
    
    :param zscore_list: List of normalised 1D images
    
    :return: List of 8-bit images
    """
    
    float_list = []
    for ind in range(len(zscore_list)):
        float_list.append(rescale_intensity(zscore_list[ind]))
        
        
    uint8_list = []
    for ind in range(len(float_list)):
        uint8_list.append(img_as_ubyte(float_list[ind]))

    return uint8_list

def segment_to_image(bits8_list, mask_list):
    """
    Transforming segments back to full 1D images based binary 1D masks
    
    :param bits8_list: List of 8-bit segments
    :param mask_list: List of binary 1D masks
    
    :return: 1D images of the segments
    """
    
    uint8 = []
    u8_copy = deepcopy(bits8_list)
    dim=256*256*120
    
    for ind in range(len(u8_copy)):
        uint8.append(np.full(dim, 0))   
        
        for value in range(len(uint8[ind])):    
            if mask_list[ind][value] == 1:
                uint8[ind][value] = u8_copy[ind][0]
                u8_copy[ind] = np.delete(u8_copy[ind],[0])
                
    return uint8
            

if __name__=="__main__":
    # The structures to be autoscaled:
    brain_parts = ['caudate', 'hippocampus', 'pallidum', 'putamen', 'thalamus' ]
    
    
    # The autoscaling process:
    for brain in brain_parts:
        
    
        # The paths:
        path_image=[r'D:\Master_2020\Data\Segmented data\children\MPH\image\bl\nifti',
                    r'D:\Master_2020\Data\Segmented data\children\placebo\image\bl\nifti',
                    r'D:\Master_2020\Data\Segmented data\children\MPH\image\bl\nifti',
                    r'D:\Master_2020\Data\Segmented data\children\placebo\image\bl\nifti',
                    r'D:\Master_2020\Data\Segmented data\children\MPH\image\pt\nifti',
                    r'D:\Master_2020\Data\Segmented data\children\placebo\image\pt\nifti',
                    r'D:\Master_2020\Data\Segmented data\children\MPH\image\pt\nifti',
                    r'D:\Master_2020\Data\Segmented data\children\placebo\image\pt\nifti']
        
        path_mask = ['D:/Master_2020/Data/Segmented data/children/MPH/mask/left_'+brain+'/bl/nifti',
                     'D:/Master_2020/Data/Segmented data/children/placebo/mask/left_'+brain+'/bl/nifti',
                     'D:/Master_2020/Data/Segmented data/children/MPH/mask/right_'+brain+'/bl/nifti',
                     'D:/Master_2020/Data/Segmented data/children/placebo/mask/right_'+brain+'/bl/nifti',
                     'D:/Master_2020/Data/Segmented data/children/MPH/mask/left_'+brain+'/pt/nifti',
                     'D:/Master_2020/Data/Segmented data/children/placebo/mask/left_'+brain+'/pt/nifti',
                     'D:/Master_2020/Data/Segmented data/children/MPH/mask/right_'+brain+'/pt/nifti',
                     'D:/Master_2020/Data/Segmented data/children/placebo/mask/right_'+brain+'/pt/nifti']
        
        end_path_image=['D:/Master_2020/Data/autoscaled_data/'+brain+'/left/mph/bl/image',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/left/placebo/bl/image',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/right/mph/bl/image',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/right/placebo/bl/image',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/left/mph/pt/image',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/left/placebo/pt/image',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/right/mph/pt/image',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/right/placebo/pt/image']
        
        end_path_mask=['D:/Master_2020/Data/autoscaled_data/'+brain+'/left/mph/bl/mask',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/left/placebo/bl/mask',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/right/mph/bl/mask',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/right/placebo/bl/mask',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/left/mph/pt/mask',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/left/placebo/pt/mask',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/right/mph/pt/mask',
                        'D:/Master_2020/Data/autoscaled_data/'+brain+'/right/placebo/pt/mask']
        
        
        path_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
        
        # 1) Creating segments and new binary masks
        for path in range(len(path_image)):
            print(path_mask[path])
            
            # 1.1) Importing images and masks
            org_image_list, org_image_affine, org_image_header = import_data(path_image[path])
            org_mask_list, org_mask_affine, org_mask_header = import_data(path_mask[path])
            
            d1_org_img = dimension_3to1(org_image_list)
            d1_org_mask = dimension_3to1(org_mask_list)
            
            # 1.2) Creating segments of the brain structures
            segment_list = create_segment(D1_image=d1_org_img, D1_mask=d1_org_mask)
            
            # 1.3) Normalising and exporting the segments
            z_segments = zscore_calc(segment_list)
            z_cut_mask = threshold(d1_org_mask, z_segments)
            
            d1_mask2 = create_full_mask(z_cut_mask, d1_org_mask)   
            d3_mask2 = dimension_1to3(d1_mask2)       
            segment_list2 = create_segment(D1_image=z_segments, D1_mask=z_cut_mask)
            
            path_dict[path].append(segment_list2)
            path_dict[path].append(d1_mask2)
            path_dict[path].append(org_image_affine)
            path_dict[path].append(org_image_header)
            
            saving(d3_mask2, org_mask_affine, org_mask_header, end_path_mask[path])
        
        # 2) Identifying the global minimum
        
        global_min = 1000
        for path in path_dict:
            new_min = minimum(path_dict[path][0])
            if new_min < global_min:
                global_min = new_min
        
        # 3) Shifting and rescaling the segments to 8-bit images
        
        for path in range(len(end_path_image)):
            segment_adjusted = adjust_zscore(path_dict[path][0], global_min)
            segment_uint8 = z_to_8bits(segment_adjusted)
            uint8_list = segment_to_image(segment_uint8, path_dict[path][1])
            d3_uint8 = dimension_1to3(uint8_list)
            
            saving(d3_uint8, path_dict[path][2], path_dict[path][3], end_path_image[path])
    
            print(datetime.now().time())
        
    
    
