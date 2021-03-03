# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:59:46 2020


__author__ = 'Inger Annett Grünbeck'
__email__ = 'inger.gruenbeck@gmail.com'
"""

import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

def load_single_nifti(filename):
    """
    This module loads a single stack of images/ a single image file
    
    :param filename: The name/path of the file
    return: the loaded image with swapped axes so that the stack index is first
    """
    img = nib.load(filename).get_fdata()
    img_swap = np.swapaxes(img, 0, 2)
    return img_swap
        
def show_slices(slices, row, col, axis=1, color = 'gray'):   
    """
    This module creates a supplot of the given slices
    
    :param slices: a list of slices/defined idexes of a stack to be plottet
    :param row: number of rows in subplot
    :param col: number of columns in subplot
    :param axis: either 0 or 1. Whether the the axis should be off or on respectively
    """
    fig, axes = plt.subplots(row,col)
    
    img_ind = 0
    for i in range(row):
        for j in range(col):
            if img_ind<len(slices):
                axes[i,j].imshow(slices[img_ind], cmap=color, origin="lower")
                if not axis:
                    axes[i,j].axis('off')
            else:
                axes[i,j].imshow(np.zeros((256, 256)), cmap='gray', origin="lower")
                
            if not axis:
                    axes[i,j].axis('off')
                    
            img_ind+=1 
  
        
def brain_image(image, image_type, x=50, y=10, z=10):
    """
    The module lets the user choose what images should be displayed.
    'full_1D' will return every slice in the stack in the x direction. 
    'specific_1D' will return one slice from one direction, either x, y, z
    'specific_3D' will return one slide from every direction, x, y, z
    
    :param image: the imagestack to be used
    :param image_type: either full_1D, specific_1D or specific_3D
    :param x: stack index x
    :param y: stack index y
    :param z: stack index z
    """
    
    if image_type=='full_1D':
        slice_list = []
        for i in range(64):
            slice_list.append(image[i, :, :])
        show_slices(slice_list, 8, 8, axis=0)
        
    elif image_type=='specific_1D':
        plt.figure()
        plt.imshow(image[x, :, :], cmap="gray", origin="lower")
        
    elif image_type=='specific_3D':
        slice_0 = image[x, :, :]
        slice_1 = image[:, y, :]
        slice_2 = image[:, :, z]
        sl = [slice_0, slice_1, slice_2]
        show_slices(sl, row=1, col=len(sl))
        
    else:
        print('Wrong image_type. Choose either full_1D,\
              specific_1D or specific_3D')
                
        
if __name__== "__main__":
  """
  p001b_FA = 'E:/Master_2020/Data/epod_dti_FA_tensor/001_bl/dti_FA.nii.gz'
  p001b_MD = 'E:/Master_2020/Data/epod_dti_MD_RD_L1/001_bl/dti_MD.nii.gz'
  p001b_RD = 'E:/Master_2020/Data/epod_dti_MD_RD_L1/001_bl/dti_RD.nii.gz'
  p001b_L1 = 'E:/Master_2020/Data/epod_dti_MD_RD_L1/001_bl/dti_L1.nii.gz'
  
  FA = load_single_nifti(p001b_FA)
  brain_image(FA, 'specific_3D')
  plt.savefig('p001b_FA.png')  
  
  MD = load_single_nifti(p001b_MD)
  brain_image(MD, 'full_1D')
  plt.savefig('p001b_MD.png')
  
  RD = load_single_nifti(p001b_RD)
  brain_image(RD, 'full_1D')
  plt.savefig('p001b_RD.png')
  
  L1 = load_single_nifti(p001b_L1)
  brain_image(L1, 'full_1D')
  plt.savefig('p001b_L1.png')
  
  nifti = 'E:/Master_2020/Data/T1_freesurfer_nifti/001_TP1/sessie1_T1.nii.gz'
  nif = load_single_nifti(nifti)
  brain_image(nif, 'full_1D')
  plt.savefig('T1_nifti.png')
  """
  nifti = 'E:/Master_2020/Data/T1_freesurfer_nifti/001_TP1/sessie1_T1.nii.gz'
  nif = load_single_nifti(nifti)
  brain_image(nif, 'specific_1D')
  plt.savefig('T1_nifti.png')
  
  p001b_FA = 'E:/Master_2020/Data/epod_dti_FA_tensor/001_bl/dti_FA.nii.gz'
  FA = load_single_nifti(p001b_FA)
  brain_image(FA, 'specific_1D')
  plt.savefig('p001b_FA.png') 