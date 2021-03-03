# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:42:34 2020

@author: inger
"""

import os
import nibabel as nib
import nrrd

#-------------------------image------------------------------------------------
"""
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\image\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)
"""               
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\image\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)
            
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\image\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
                
                
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\image\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)  

#---------------caudate--------------------------------------------------------------
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_caudate\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_caudate\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_caudate\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_caudate\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)  
                
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_caudate\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_caudate\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_caudate\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_caudate\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)

#----------------hippocampus-----------------------------------------------------
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_hippocampus\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_hippocampus\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_hippocampus\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_hippocampus\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)  
                
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_hippocampus\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_hippocampus\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_hippocampus\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_hippocampus\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data) 

#----------------pallidum---------------------------------------------------------     
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_pallidum\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_pallidum\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_pallidum\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_pallidum\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)  
                
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_pallidum\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_pallidum\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_pallidum\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_pallidum\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data) 
                
#----------------putamen---------------------------------------------------------     
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_putamen\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_putamen\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_putamen\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_putamen\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)  
                
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_putamen\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_putamen\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_putamen\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_putamen\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
                
#----------------putamen---------------------------------------------------------     
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_thalamus\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_left_thalamus\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_thalamus\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\MPH\mask_right_thalamus\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)  
                
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_thalamus\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   

path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_left_thalamus\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)     


path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_thalamus\TP1'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)   
    
            
path= r'D:\Master_2020\Data\Segmented data_nrrdunfit_niifit\children\placebo\mask_right_thalamus\TP2'
for dirname, _, filenames in os.walk(path):
    if filenames:
        for file in filenames:
            if 'nii' in file:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write(path + '/nrrd/' + file[:-4] +'.nrrd', file_data)                 