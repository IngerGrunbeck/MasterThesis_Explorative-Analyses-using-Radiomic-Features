# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:44:00 2020

__author__ = 'Inger Annett Grünbeck'
__email__ = 'inger.gruenbeck@gmail.com'
"""
from imaging_data import show_slices
from intensity_hist import intensity_hist

import nibabel as nib
import numpy as np
import os
import matplotlib.pyplot as plt
from copy import deepcopy
from scipy.stats import zscore
from skimage import img_as_ubyte
from skimage.exposure import rescale_intensity


"""
This script uses the baseline images of MPH treated children
"""

#%% 1) Import images and masks into a list for each

image_list = []
image_affine = []
image_header = []

path_data = r'D:\Master_2020\TEST_caudate\MPH\images\bl\nifti'
for dirname, _, filenames in os.walk(path_data):
    for file in sorted(filenames):
        img = nib.load(os.path.join(dirname, file))
        image = img.get_fdata()
        image_swap = np.transpose(image)
        image_list.append(image_swap)
        image_affine.append(img.affine)
        image_header.append(img.header)

       
mask_list = []
mask_affine = []
mask_header = []

path_data = r'D:\Master_2020\TEST_caudate\MPH\masks\bl\nifti'
for dirname, _, filenames in os.walk(path_data):
    for file in sorted(filenames):
        mask = nib.load(os.path.join(dirname, file))
        ma = mask.get_fdata()
        mask_swap = np.transpose(ma)
        mask_list.append(mask_swap)
        mask_affine.append(mask.affine)
        mask_header.append(mask.header)
                          
#%% 2) Plotting the masks

slice_mask = []
for image in mask_list:
    slice_mask.append(image[60])
    
show_slices(slice_mask, 4, 6, axis=0)

#%% 3) Creating a segmented image and plotting it. 
# The first part should only be done if no segmented, unscaled images exist. 
#If they do, import them instead

if os.path.isfile(r'D:\Master_2020\TEST_caudate\MPH\segmented\bl\0_seg.nii'):
    #import the files
    seg_original = []
    seg_affine = []
    seg_header = []
    
    path_data = r'D:\Master_2020\TEST_caudate\MPH\segmented\bl'
    for dirname, _, filenames in os.walk(path_data):
        for file in sorted(filenames):
            seg = nib.load(os.path.join(dirname, file))
            seg_img = seg.get_fdata()
            seg_swap = np.transpose(seg_img)
            seg_original.append(seg_swap)
            seg_affine.append(seg.affine)
            seg_header.append(seg.header)
    
else:
    seg_original = deepcopy(image_list)
    
    
    for volume in range(len(seg_original)):
        for slices in range(seg_original[volume].shape[0]):
            for row in range(seg_original[volume].shape[1]):
                for col in range(seg_original[volume].shape[2]):
                    if mask_list[volume][slices][row][col] == 0:
                        seg_original[volume][slices][row][col] = 0
        

#%% 4) Plotting the unscaled segment and the intensity histogram of the first image
                    
slice_seg = []
for image in seg_original:
    slice_seg.append(image[60])
    
show_slices(slice_seg, 4, 6, axis=0, color='hot')


intensity_hist(seg_original[0], hist_length=1400)

#%% 5) Reading the segmented images to nifti images and store them for later
    #We use the affine and the header of the original images.
    #Before saving the segmented files we check whether there already exist images in the folder

if os.path.isfile(r'D:\Master_2020\TEST_caudate\MPH\segmented\bl\0_seg.nii') is False:
    for index in range(len(seg_original)):
        transposed = np.transpose(seg_original[index])
        temp_seg = nib.Nifti1Image(transposed, image_affine[index], image_header[index])
        if index < 10:
            name = 'D:/Master_2020/TEST_caudate/MPH/segmented/bl/00'+str(index)+'_seg.nii'
        elif index >= 10 and index < 100:
            name = 'D:/Master_2020/TEST_caudate/MPH/segmented/bl/0'+str(index)+'_seg.nii'
        else:
            name = 'D:/Master_2020/TEST_caudate/MPH/segmented/bl/'+str(index)+'_seg.nii'
        nib.save(temp_seg, name)
    
    
    
#%% 7) Reshaping the brain images and the masks into 1D shapes

D1_brain = []
shape = image_list[0].shape
dim = shape[0]*shape[1]*shape[2]

for element in image_list:
    D1_brain.append(np.reshape(element, (dim,1)))
    
D1_mask = []
for element in mask_list:
    D1_mask.append(np.reshape(element, (dim,1)))
        
#%% 8) Create a list of arrays containing only the segmented values 
    
D1_seg= []
volume = 0

for element in D1_brain:
    val_ind = 0
    D1_seg.append(np.zeros(0))
    
    for value in element:
        if D1_mask[volume][val_ind] == 1:
            D1_seg[volume] = np.append(D1_seg[volume], value)
        val_ind += 1
        
    volume += 1


#%% 9) Calculate z scores for segment

segment_z = []
for ind in range(len(D1_seg)):
    segment_z.append(zscore(D1_seg[ind]))
    
    
#%% 10) check for max and min in every image
min_seg = []
max_seg  = []

for element in segment_z:
    min_seg.append(element.min())
    max_seg.append(element.max())

#%% 11) Global min max
    
global_min = 0
global_max = 0

for element in min_seg:
    if element<= global_min:
        global_min = element
        
for element in max_seg:
    if element >= global_max:
        global_max = element
        
#%% 12) Adding global min to every element
        
seg_z_adjusted = []

for ind in range(len(segment_z)):
    seg_z_adjusted.append(segment_z[ind] - global_min)
    
#%% 13) Scale the images down to gray scale using img_as_float
    
seg_float = []

for ind in range(len(seg_z_adjusted)):
    seg_float.append(rescale_intensity(seg_z_adjusted[ind]))
    

#%% 14) convert image to 8 bits, 6 bits and 7 bits image using img_as_ubyte
    
seg_uint8 = []

for ind in range(len(seg_float)):
    seg_uint8.append(img_as_ubyte(seg_float[ind]))

seg_uint7 = []
seg_uint6 = []

for ind in range(len(seg_uint8)):
    seg_uint7.append(seg_uint8[ind]/2)
    seg_uint7[ind] = seg_uint7[ind].astype('uint8')
    
    seg_uint6.append(seg_uint8[ind]/4)
    seg_uint6[ind] = seg_uint6[ind].astype('uint8')
    
    
    
#%% 15) Trackback segmentation to -1 image

uint8 = []
u8_copy = deepcopy(seg_uint8)

for ind in range(len(u8_copy)):
    uint8.append(np.full(dim, 0))   
    for value in range(len(uint8[ind])):    
        if D1_mask[ind][value] == 1:
            uint8[ind][value] = u8_copy[ind][0]
            u8_copy[ind] = np.delete(u8_copy[ind],[0])
            
#%% Doing step 15) for 6 and 7 bits images
            
uint7 = []
u7_copy = deepcopy(seg_uint7)

for ind in range(len(u7_copy)):
    uint7.append(np.full(dim, 0))   
    for value in range(len(uint7[ind])):    
        if D1_mask[ind][value] == 1:
            uint7[ind][value] = u7_copy[ind][0]
            u7_copy[ind] = np.delete(u7_copy[ind],[0])
            
uint6 = []
u6_copy = deepcopy(seg_uint6)

for ind in range(len(u6_copy)):
    uint6.append(np.full(dim, 0))   
    for value in range(len(uint6[ind])):    
        if D1_mask[ind][value] == 1:
            uint6[ind][value] = u6_copy[ind][0]
            u6_copy[ind] = np.delete(u6_copy[ind],[0])
            
#%% Plotting the imstensity hist of the first image again:
intensity_hist(uint8[0])
intensity_hist(uint7[0], hist_length=150)
intensity_hist(uint6[0], hist_length=70)

#%% 16) Reshape images
    
D3_seg_8 = []

for ind in range(len(uint8)):
    D3_seg_8.append(np.reshape(uint8[ind], (120, 256, 256)))
    
D3_seg_7 = []

for ind in range(len(uint7)):
    D3_seg_7.append(np.reshape(uint7[ind], (120, 256, 256)))
    
D3_seg_6 = []

for ind in range(len(uint6)):
    D3_seg_6.append(np.reshape(uint6[ind], (120, 256, 256)))
    
#%% 17) Plot histograms an images of the segments
    
slice_after_seg_8 = []
for image in D3_seg_8:
    slice_after_seg_8.append(image[60])
    
show_slices(slice_after_seg_8, 4, 6, axis=0, color='hot')

slice_after_seg_7 = []
for image in D3_seg_7:
    slice_after_seg_7.append(image[60])
    
show_slices(slice_after_seg_7, 4, 6, axis=0, color='gray')

slice_after_seg_6 = []
for image in D3_seg_6:
    slice_after_seg_6.append(image[60])
    
show_slices(slice_after_seg_6, 4, 6, axis=0, color='gray')
        

#%% Closer look at image 14, slice 60

plt.figure()
plt.imshow(seg_original[1][60], cmap='gray', origin='lower')

plt.figure()
plt.imshow(D3_seg_8[1][60], cmap='gray', origin='lower')


plt.figure()
plt.imshow(seg_original[1][60], cmap='hot', origin='lower')

plt.figure()
plt.imshow(D3_seg_8[1][60], cmap='hot', origin='lower')

plt.figure()
plt.imshow(D3_seg_7[1][60], cmap='hot', origin='lower')
plt.figure()
plt.imshow(D3_seg_7[1][60], cmap='gray', origin='lower')

plt.figure()
plt.imshow(D3_seg_6[1][60], cmap='hot', origin='lower')
plt.figure()
plt.imshow(D3_seg_6[1][60], cmap='gray', origin='lower')

#%% 18) save images 

for index in range(len(D3_seg_8)):
    transposed = np.transpose(D3_seg_8[index])
    temp_seg = nib.Nifti1Image(transposed, image_affine[index], image_header[index])
    if index < 10:
            name = 'D:/Master_2020/TEST_caudate/MPH/8bits/bl/00'+str(index)+'_seg.nii'
    elif index >= 10 and index < 100:
        name = 'D:/Master_2020/TEST_caudate/MPH/8bits/bl/0'+str(index)+'_seg.nii'
    else:
        name = 'D:/Master_2020/TEST_caudate/MPH/8bits/bl/'+str(index)+'_seg.nii'
    nib.save(temp_seg, name)


for index in range(len(D3_seg_7)):
    transposed = np.transpose(D3_seg_7[index])
    temp_seg = nib.Nifti1Image(transposed, image_affine[index], image_header[index])
    if index < 10:
            name = 'D:/Master_2020/TEST_caudate/MPH/7bits/bl/00'+str(index)+'_seg.nii'
    elif index >= 10 and index < 100:
        name = 'D:/Master_2020/TEST_caudate/MPH/7bits/bl/0'+str(index)+'_seg.nii'
    else:
        name = 'D:/Master_2020/TEST_caudate/MPH/7bits/bl/'+str(index)+'_seg.nii'
    nib.save(temp_seg, name)


for index in range(len(D3_seg_6)):
    transposed = np.transpose(D3_seg_6[index])
    temp_seg = nib.Nifti1Image(transposed, image_affine[index], image_header[index])
    if index < 10:
            name = 'D:/Master_2020/TEST_caudate/MPH/6bits/bl/00'+str(index)+'_seg.nii'
    elif index >= 10 and index < 100:
        name = 'D:/Master_2020/TEST_caudate/MPH/6bits/bl/0'+str(index)+'_seg.nii'
    else:
        name = 'D:/Master_2020/TEST_caudate/MPH/6bits/bl/'+str(index)+'_seg.nii'
    nib.save(temp_seg, name)
