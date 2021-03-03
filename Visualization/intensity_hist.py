# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:57:49 2020

@author: inger
"""
import numpy as np
import matplotlib.pyplot as plt

def intensity_hist(image, new_figure=True, hist_length = 256):
    shape=np.shape(image)
    if len(shape) == 3:
        shape = (shape[0]*shape[1]*shape[2],1)
        image = np.reshape(image, shape[0])
        
    hist_seg = np.zeros(hist_length)
        

    for i in range(shape[0]):
        pixval_seg = int(image[i])
        if pixval_seg != 0: 
            hist_seg[pixval_seg] += 1
      
    if new_figure:
        plt.figure()
    plt.plot(hist_seg)
    
def float_hist(image, zero=False):
    liste = list(image)
    counter = []
    unique = np.unique(liste)
    unique = list(unique)
    if zero:
        unique.remove(0)
        
    for element in unique:
        counter.append(liste.count(element))
        
    plt.figure()
    plt.plot(unique, counter)
    plt.ylabel('Number of voxels')
    plt.xlabel('Intensity value of voxels')
    plt.show()
    
        