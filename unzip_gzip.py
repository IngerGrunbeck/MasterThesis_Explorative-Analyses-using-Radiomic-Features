# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:44:00 2020

__author__ = 'Inger Annett Grünbeck'
__email__ = 'inger.gruenbeck@gmail.com'
"""

import gzip
import shutil
import os

path_data= r'D:\Master_2020\Data\nye data_feb\zipped'


for dirname, _, filenames in os.walk(path_data):
    if filenames:
        new_path = 'D:/Master_2020/Data/nye data_feb/unzipped/'+ dirname[-7:]+'/'
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            
        for file in sorted(filenames):
            if file.endswith(".gz"):
                with gzip.open(os.path.join(dirname, file), 'rb') as f_in:
                    with open(new_path+file[:-3], 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)

    

