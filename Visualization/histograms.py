# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:39:13 2020

@author: inger
"""

import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import autoscaling_def as auto
import intensity_hist as hist 

SMALL_SIZE = 18
MEDIUM_SIZE = 22
BIGGER_SIZE = 24

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title

img = nib.load(r'D:\Master_2020\Data\autoscaled_data\caudate\left\mph\bl\image\000_seg.nii')
image = img.get_fdata()
image_swap = np.transpose(image)
image_list = []
image_list.append(image_swap)


mask_list = []
mask = nib.load(r'D:\Master_2020\Data\Segmented data\children\test_segments_mph_bl\000_seg.nii')
ma = mask.get_fdata()
mask_swap = np.transpose(ma)
mask_list.append(mask_swap)


#dim1_image = auto.dimension_3to1(image_list)
#dim1_mask = auto.dimension_3to1(mask_list)

#hist.float_hist(dim1_image[0], zero=True)   


img_cut = []
for row in range(120,180):
    img_cut.append(image_list[0][55][row][110:170])
segment_img = []
for row in range(120,180):
    segment_img.append(mask_list[0][55][row][110:170])


fig, ax = plt.subplots(subplot_kw={'xticks': [], 'yticks': []})
main = ax.imshow(img_cut, cmap='hot', origin='lower', alpha=1)
#seg = ax.imshow(segment_img, cmap='hot', origin='lower', alpha=1)
plt.tight_layout
cbar = ax.figure.colorbar(main, ax=ax)
cbar.ax.set_ylabel('Intensity of voxels', rotation=-90, va="bottom")





