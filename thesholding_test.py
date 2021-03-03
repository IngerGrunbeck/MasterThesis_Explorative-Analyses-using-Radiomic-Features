# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:39:46 2020

@author: inger
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
                          
        
D1_brain = []
shape = image_list[0].shape
dim = shape[0]*shape[1]*shape[2]

D1_brain = []
shape = image_list[0].shape
dim = shape[0]*shape[1]*shape[2]

for element in image_list:
    D1_brain.append(np.reshape(element, (dim,1)))
    
D1_mask = []
for element in mask_list:
    D1_mask.append(np.reshape(element, (dim,1)))
   
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

segment_z = []
for ind in range(len(D1_seg)):
    segment_z.append(zscore(D1_seg[ind]))

#%% Thresholding the mask

new_mask = []
for ind in range(len(D1_mask)):
    new_mask.append(np.ones(int(D1_mask[ind].sum())))

for element in range(len(segment_z)):
    for ind in range(len(segment_z[element])):
        if segment_z[element][ind] <-3:
            new_mask[element][ind] = 0
        elif segment_z[element][ind] > 3:
            new_mask[element][ind] = 0

#%% Back to square 1
new_mb = deepcopy(D1_mask)
n_m = deepcopy(new_mask)

for ind in range(len(D1_mask)):
    for value in range(len(D1_mask[ind])):    
        if D1_mask[ind][value] == 1:
            new_mb[ind][value] = n_m[ind][0]
            n_m[ind] = np.delete(n_m[ind],[0])

#%% transforming the mask back
D3_new_mask = []

for ind in range(len(new_mb)):
    D3_new_mask.append(np.reshape(new_mb[ind], (120, 256, 256)))
            
for index in range(len(D3_new_mask)):
    transposed = np.transpose(D3_new_mask[index])
    temp_seg = nib.Nifti1Image(transposed, mask_affine[index], mask_header[index])
    if index < 10:
        name = 'D:/Master_2020/TEST_caudate/MPH/new_mask/bl/00'+str(index)+'_seg.nii'
    elif index >= 10 and index < 100:
        name = 'D:/Master_2020/TEST_caudate/MPH/new_mask/bl/0'+str(index)+'_seg.nii'
    else:
        name = 'D:/Master_2020/TEST_caudate/MPH/new_mask/bl/'+str(index)+'_seg.nii'
    nib.save(temp_seg, name)

#%%creating segments based on new mask
D1_new_seg= []
volume = 0

for element in segment_z:
    val_ind = 0
    D1_new_seg.append(np.zeros(0))
    
    for value in element:
        if new_mask[volume][val_ind] == 1:
            D1_new_seg[volume] = np.append(D1_new_seg[volume], value)
        val_ind += 1
        
    volume += 1  
   

#%% z_adjusted
min_seg = []
max_seg  = []

for element in D1_new_seg:
    min_seg.append(element.min())
    max_seg.append(element.max())
    
global_min = 0
global_max = 0

for element in min_seg:
    if element<= global_min:
        global_min = element
        
for element in max_seg:
    if element >= global_max:
        global_max = element
            
seg_adjusted = []
for ind in range(len(D1_new_seg)):
    seg_adjusted.append(D1_new_seg[ind] - global_min)



#%% to image, replace name n for loop
   
    
seg_float = []

for ind in range(len(seg_adjusted)):
    seg_float.append(rescale_intensity(seg_adjusted[ind]))
    
    
seg_uint8 = []

for ind in range(len(seg_float)):
    seg_uint8.append(img_as_ubyte(seg_float[ind]))
    


uint8 = []
u8_copy = deepcopy(seg_uint8)

for ind in range(len(u8_copy)):
    uint8.append(np.full(dim, 0))   
    for value in range(len(uint8[ind])):    
        if new_mb[ind][value] == 1:
            uint8[ind][value] = u8_copy[ind][0]
            u8_copy[ind] = np.delete(u8_copy[ind],[0])
            

D3_seg_8 = []

for ind in range(len(uint8)):
    D3_seg_8.append(np.reshape(uint8[ind], (120, 256, 256)))



#%%     
slice_after_seg_8 = []
for image in D3_seg_8:
    slice_after_seg_8.append(image[60])
    
#%% 
    
show_slices(slice_after_seg_8, 4, 6, axis=0, color='hot')

plt.figure()
plt.imshow(D3_seg_8[1][60], cmap='hot', origin='lower')

for index in range(len(D3_seg_8)):
    transposed = np.transpose(D3_seg_8[index])
    temp_seg = nib.Nifti1Image(transposed, image_affine[index], image_header[index])
    if index < 10:
        name = 'D:/Master_2020/TEST_caudate/MPH/8bit_new_mask/bl/00'+str(index)+'_seg.nii'
    elif index >= 10 and index < 100:
        name = 'D:/Master_2020/TEST_caudate/MPH/8bit_new_mask/bl/0'+str(index)+'_seg.nii'
    else:
        name = 'D:/Master_2020/TEST_caudate/MPH/8bit_new_mask/bl/'+str(index)+'_seg.nii'
    nib.save(temp_seg, name)

    
#%% 
    
