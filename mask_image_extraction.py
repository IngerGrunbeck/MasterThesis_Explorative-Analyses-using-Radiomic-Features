# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:53:16 2020

__author__ = 'Inger Annett Grünbeck'
__email__ = 'inger.gruenbeck@gmail.com'
"""

import nibabel as nib
import os 
import nrrd
import numpy as np


path_data = 'D:/Master_2020/Unzipped_data+nifti_mask/T1'

for dirname, _, filenames in os.walk(path_data):
    if filenames:
        for file in filenames:
            left_hip = file.find('Left-H')
            right_hip = file.find('Right-H')
            left_thal = file.find('Left-T')
            right_thal = file.find('Right-T')

            left_cau = file.find('Left-Cau')
            right_cau = file.find('Right-Cau')
            left_pal = file.find('Left-Pa')
            right_pal = file.find('Right-Pa')
            left_put = file.find('Left-Pu')
            right_put = file.find('Right-Pu')
            
            image = file.find('T1')
           
            if left_hip>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata()                
                nrrd.write('D:/Master_2020/Segmented data/mask_left_hippocampus/'+ dirname[-7:] + '_Left_Hippocampus.nrrd', file_data)
           
            elif right_hip>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write('D:/Master_2020/Segmented data/mask_right_hippocampus/'+ dirname[-7:] + '_Right_Hippocampus.nrrd', file_data)
            
            elif right_thal>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata()                
                nrrd.write('D:/Master_2020/Segmented data/mask_right_thalamus/'+ dirname[-7:] + '_Right_Thalamus.nrrd', file_data)
            
            elif left_thal>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata()                
                nrrd.write('D:/Master_2020/Segmented data/mask_left_thalamus/'+ dirname[-7:] + '_Left_Thalamus.nrrd', file_data)
     
            if left_cau>=0:
                print(file)
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write('D:/Master_2020/Segmented data/mask_left_caudate/'+ dirname[-7:] + '_Left_Caudate.nrrd', file_data)
          
            elif right_cau>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata() 
                nrrd.write('D:/Master_2020/Segmented data/mask_right_caudate/'+ dirname[-7:] + '_Right_Caudate.nrrd', file_data)
            
            elif right_pal>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata()                
                nrrd.write('D:/Master_2020/Segmented data/mask_right_pallidum/'+ dirname[-7:] + '_Right_Pallidum.nrrd', file_data)
            
            elif left_pal>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata()                
                nrrd.write('D:/Master_2020/Segmented data/mask_left_pallidum/'+ dirname[-7:] + '_Left_Pallidum.nrrd', file_data)
            
              
            elif right_put>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata()                
                nrrd.write('D:/Master_2020/Segmented data/mask_right_putamen/'+ dirname[-7:] + '_Right_Putamen.nrrd', file_data)
            
            elif left_put>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata()                
                nrrd.write('D:/Master_2020/Segmented data/mask_left_putamen/'+ dirname[-7:] + '_Left_Putamen.nrrd', file_data)
            
            
            elif image>=0:
                file_load = nib.load(os.path.join(dirname, file))
                file_data = file_load.get_fdata()
                nrrd.write('D:/Master_2020/Segmented data/image/'+ dirname[-7:] + '_T1.nrrd', file_data)
            
            """

    
