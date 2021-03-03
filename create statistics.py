# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:06:56 2020

@author: inger
"""

import nibabel as nib
import numpy as np
import os
import matplotlib.pyplot as plt
import autoscaling_def as auto
import statistics as stats

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

structure_org = ['/left_caudate', '/right_caudate',
                 '/left_hippocampus', '/right_hippocampus',
                 '/left_pallidum', '/right_pallidum',
                 '/left_putamen', '/right_putamen',
                 '/left_thalamus', '/right_thalamus']

structure_seg = ['/caudate/left', '/caudate/right',
                 '/hippocampus/left', '/hippocampus/right',
                 '/pallidum/left', '/pallidum/right',
                 '/putamen/left', '/putamen/right',
                 '/thalamus/left', '/thalamus/right'
                 ]

structure_title = ['left caudate', 'right caudate',
                   'left hippocampus', 'right hippocampus',
                   'left pallidum', 'right pallidum',
                   'left putamen', 'right putamen',
                   'left thalamus', 'right thalamus']

week = ['/bl', '/pt']

for structure in range(len(structure_org)):
    image_org_list = [[], [], [], []]
    mask_org_list = [[], [], [], []]
    org_segments = [[], [], [], []]
    
    dim1_org_image = [[], [], [], []]
    dim1_org_mask = [[], [], [], []]
    
    min_int = [[], [], [], []]
    max_int= [[], [], [], []]
    mean_int = [[], [], [], []]
    
    for outer_ind in range(2):
        paths_img_org = ['D:/Master_2020/Data/Segmented data/children/MPH/image' + week[outer_ind] +'/nifti',
                     'D:/Master_2020/Data/Segmented data/children/placebo/image' + week[outer_ind] +'/nifti']
        paths_masks_org = ['D:/Master_2020/Data/Segmented data/children/MPH/mask' + structure_org[structure] + week[outer_ind] +'/nifti',
                       'D:/Master_2020/Data/Segmented data/children/placebo/mask' + structure_org[structure] + week[outer_ind] +'/nifti']
        
        for inner_ind in range(len(paths_img_org)): 
        
            for dirname, _, filenames in os.walk(paths_img_org[inner_ind]):
                for file in sorted(filenames):
                    img = nib.load(os.path.join(dirname, file))
                    image = img.get_fdata()
                    image_swap = np.transpose(image)
                    image_org_list[outer_ind].append(image_swap)
              
                
            for dirname, _, filenames in os.walk(paths_masks_org[inner_ind]):
                for file in sorted(filenames):
                    mask = nib.load(os.path.join(dirname, file))
                    ma = mask.get_fdata()
                    mask_swap = np.transpose(ma)
                    mask_org_list[outer_ind].append(mask_swap)
        
        
        paths_img = ['D:/Master_2020/Data/autoscaled_data' + structure_seg[structure] +'/mph' + week[outer_ind] +'/image',
                     'D:/Master_2020/Data/autoscaled_data' + structure_seg[structure] +'/placebo' + week[outer_ind] +'/image'] 
        paths_masks = ['D:/Master_2020/Data/autoscaled_data' + structure_seg[structure] +'/mph' + week[outer_ind] +'/mask',
                       'D:/Master_2020/Data/autoscaled_data' + structure_seg[structure] +'/placebo' + week[outer_ind] +'/mask']
        
        for inner_ind in range(len(paths_img)): 
        
            for dirname, _, filenames in os.walk(paths_img[inner_ind]):
                for file in sorted(filenames):
                    img = nib.load(os.path.join(dirname, file))
                    image = img.get_fdata()
                    image_swap = np.transpose(image)
                    image_org_list[outer_ind+2].append(image_swap)
              
                
            for dirname, _, filenames in os.walk(paths_masks[inner_ind]):
                for file in sorted(filenames):
                    mask = nib.load(os.path.join(dirname, file))
                    ma = mask.get_fdata()
                    mask_swap = np.transpose(ma)
                    mask_org_list[outer_ind+2].append(mask_swap)
                    
        
    for ind in range(4):
        dim1_org_image[ind] = auto.dimension_3to1(image_org_list[ind])
        dim1_org_mask[ind] = auto.dimension_3to1(mask_org_list[ind])

        org_segments[ind] = auto.create_segment(D1_image=dim1_org_image[ind], D1_mask=dim1_org_mask[ind])
        
        for element in org_segments[ind]:
            min_int[ind].append(min(element))
            max_int[ind].append(max(element))
            mean_int[ind].append(stats.mean(element))
        
        
    

    ids = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
    figure, axes = plt.subplots(nrows=2, ncols=2)
    
    axes[0, 0].scatter(ids,min_int[0], label='Min')
    axes[0, 0].scatter(ids,max_int[0], label='Max')
    axes[0, 0].scatter(ids,mean_int[0], label='Mean')
    axes[0, 1].scatter(ids,min_int[1], label='Min')
    axes[0, 1].scatter(ids,max_int[1], label='Max')
    axes[0, 1].scatter(ids,mean_int[1], label='Mean')
    axes[1, 0].scatter(ids,min_int[2], label='Min')
    axes[1, 0].scatter(ids,max_int[2], label='Max')
    axes[1, 0].scatter(ids,mean_int[2], label='Mean')
    axes[1, 1].scatter(ids,min_int[3], label='Min')
    axes[1, 1].scatter(ids,max_int[3], label='Max')
    axes[1, 1].scatter(ids,mean_int[3], label='Mean')
    
    figure.gca().legend(loc='center left', bbox_to_anchor=(1, 1.1), ncol=1)
    #axes[0, 1].gca().legend(ncol=3,loc='center', bbox_to_anchor=(0.5, 1.05))
    #axes[1, 0].gca().legend(ncol=3,loc='center', bbox_to_anchor=(0.5, 1.05))
    #axes[1, 1].gca().legend(ncol=3,loc='center', bbox_to_anchor=(0.5, 1.05))
    
    
    axes[0, 0].set_title('Pre-treatment statistics before autoscaling')
    axes[0, 1].set_title('Post-treatment statistics before autoscaling')
    axes[1, 0].set_title('Pre-treatment statistics after autoscaling')
    axes[1, 1].set_title('Post-treatment statistics after autoscaling')
    
    figure.suptitle('Intensity statistics of the '+structure_title[structure])
    
    for ax in axes.flat:
        ax.set(xlabel='Participant ID', ylabel='Intensity')
    for ax in axes.flat:
        ax.label_outer()
        
    plt.show()
        
    
        
    
    


