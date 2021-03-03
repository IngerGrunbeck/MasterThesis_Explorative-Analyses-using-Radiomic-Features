# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:18:23 2020

@author: inger
"""

import os 


def rename(general_path, file_name, new_dir):
    for dirname, _, filenames in os.walk(general_path):
        if filenames:
            for file in filenames:
                if file_name in file:
                    old_path = os.path.join(dirname, file)
                    
                    if file_name == '_pt':
                        new_name = file[0:6] + '.nii'
                        new_path = os.path.join(new_dir, new_name)
                        if os.path.isfile(new_path) is False:
                            os.rename(old_path, new_path)
                            
                    elif file_name == '_bl':
                        new_name = file[0:6] + '.nii'
                        new_path = os.path.join(new_dir, new_name)
                        if os.path.isfile(new_path) is False:
                            os.rename(old_path, new_path)
                            
                    elif general_path[-2:]=='bl':
                        new_name = dirname[-7:-4] +'_bl.nii'
                        new_path = os.path.join(new_dir, new_name)
                        if os.path.isfile(new_path) is False:
                            os.rename(old_path, new_path)
                            
                    elif general_path[-2:]=='pt':
                        new_name = dirname[-7:-4] + '_pt.nii'
                        new_path = os.path.join(new_dir, new_name)
                        if os.path.isfile(new_path) is False:
                            os.rename(old_path, new_path)
                        
if __name__== "__main__":
    #image
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='_bl', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\images\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='_pt', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\images\pt\nifti')
    #caudate
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Left-Caudate.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_caudate\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Right-Caudate.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_caudate\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Left-Caudate.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_caudate\pt\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Right-Caudate.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_caudate\pt\nifti')
    
    #hippocampus
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Left-Hippocampus.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_hippocampus\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Right-Hippocampus.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_hippocampus\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Left-Hippocampus.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_hippocampus\pt\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Right-Hippocampus.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_hippocampus\pt\nifti')
    
    #pallidum
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Left-Pallidum.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_pallidum\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Right-Pallidum.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_pallidum\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Left-Pallidum.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_pallidum\pt\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Right-Pallidum.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_pallidum\pt\nifti')
    
    #putamen
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Left-Putamen.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_putamen\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Right-Putamen.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_putamen\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Left-Putamen.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_putamen\pt\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Right-Putamen.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_putamen\pt\nifti')
    
    #thalamus
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Left-Thalamus-Proper.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_thalamus\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\bl', 
           file_name='resampled_Right-Thalamus-Proper.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_thalamus\bl\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Left-Thalamus-Proper.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\left_thalamus\pt\nifti')
    
    rename(general_path=r'D:\Master_2020\Data\Unzipped_data+nifti_mask\sorted\adult_plac\pt', 
           file_name='resampled_Right-Thalamus-Proper.nii', 
           new_dir=r'D:\Master_2020\Data\Segmented data\Adult\placebo\right_thalamus\pt\nifti')
   
