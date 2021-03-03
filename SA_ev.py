# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:00:40 2020

@author: inger
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import statistics as stats
import matplotlib.ticker as ticker

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

df_ca_bbl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_bl_caudate.csv')
df_hip_bbl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_bl_hippocampus.csv')
df_pal_bbl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_bl_pallidum.csv')
df_pu_bbl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_bl_putamen.csv')
df_thal_bbl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_bl_thalamus.csv')

df_ca_bpt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_pt_caudate.csv')
df_hip_bpt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_pt_hippocampus.csv')
df_pal_bpt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_pt_pallidum.csv')
df_pu_bpt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_pt_putamen.csv')
df_thal_bpt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_before autoscale\children\shape_pt_thalamus.csv')

df_ca_abl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\caudate_bl_shape.csv')
df_hip_abl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\hippocampus_bl_shape.csv')
df_pal_abl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\pallidum_bl_shape.csv')
df_pu_abl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\putamen_bl_shape.csv')
df_thal_abl = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\thalamus_bl_shape.csv')

df_ca_apt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\caudate_pt_shape.csv')
df_hip_apt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\hippocampus_pt_shape.csv')
df_pal_apt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\pallidum_pt_shape.csv')
df_pu_apt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\putamen_pt_shape.csv')
df_thal_apt = pd.read_csv(r'D:\Master_2020\Extracted Features\Shape_after autoscale_children\thalamus_pt_shape.csv')


structures = ['The Caudate', ' The Hippocampus', 'The Pallidum', 'The Putamen', 'The Thalamus']

ca_bl = (df_ca_abl-df_ca_bbl)*100/df_ca_bbl
hip_bl = (df_hip_abl-df_hip_bbl)*100/df_hip_bbl
pal_bl = (df_pal_abl-df_pal_bbl)*100/df_pal_bbl
pu_bl = (df_pu_abl-df_pu_bbl)*100/df_pu_bbl
thal_bl = (df_thal_abl-df_thal_bbl)*100/df_thal_bbl

ca_pt = (df_ca_apt-df_ca_bpt)*100/df_ca_bpt
hip_pt = (df_hip_apt-df_hip_bpt)*100/df_hip_bpt
pal_pt = (df_pal_apt-df_pal_bpt)*100/df_pal_bpt
pu_pt = (df_pu_apt-df_pu_bpt)*100/df_pu_bpt
thal_pt =  (df_thal_apt-df_thal_bpt)*100/df_thal_bpt

bl = [ca_bl, hip_bl, pal_bl, pu_bl, thal_bl]
pt = [ca_pt, hip_pt, pal_pt, pu_pt, thal_pt]



for structure in range(len(structures)):  
    
    ids = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
    figure, axes = plt.subplots(nrows=2, ncols=2)
    print(stats.mean([stats.mean(bl[structure].loc[:,'SurfaceArea_left']),
    stats.mean(bl[structure].loc[:,'SurfaceArea_right']),
    stats.mean(pt[structure].loc[:,'SurfaceArea_left']),
    stats.mean(pt[structure].loc[:,'SurfaceArea_right'])]))a
    print('------------------------------')
    
    
    axes[0, 0].scatter(ids,bl[structure].loc[:,'SurfaceArea_left'])
    axes[0, 0].plot(ids, [stats.mean(bl[structure].loc[:,'SurfaceArea_left'])]*len(ids), 'k')
    axes[0, 0].plot(ids, [stats.mean(bl[structure].loc[:,'SurfaceArea_left'])+ 3*stats.stdev(bl[structure].loc[:,'SurfaceArea_left'])]*len(ids), 'r')
    axes[0, 0].plot(ids, [stats.mean(bl[structure].loc[:,'SurfaceArea_left'])- 3*stats.stdev(bl[structure].loc[:,'SurfaceArea_left'])]*len(ids), 'r')

    axes[0, 1].scatter(ids,bl[structure].loc[:,'SurfaceArea_right'])
    axes[0, 1].plot(ids, [stats.mean(bl[structure].loc[:,'SurfaceArea_right'])]*len(ids), 'k')
    axes[0, 1].plot(ids, [stats.mean(bl[structure].loc[:,'SurfaceArea_right'])+ 3*stats.stdev(bl[structure].loc[:,'SurfaceArea_right'])]*len(ids), 'r')
    axes[0, 1].plot(ids, [stats.mean(bl[structure].loc[:,'SurfaceArea_right'])- 3*stats.stdev(bl[structure].loc[:,'SurfaceArea_right'])]*len(ids), 'r')
    
    axes[1, 0].scatter(ids,pt[structure].loc[:,'SurfaceArea_left'])
    axes[1, 0].plot(ids, [stats.mean(pt[structure].loc[:,'SurfaceArea_left'])]*len(ids), 'k')
    axes[1, 0].plot(ids, [stats.mean(pt[structure].loc[:,'SurfaceArea_left'])+ 3*stats.stdev(pt[structure].loc[:,'SurfaceArea_left'])]*len(ids), 'r')
    axes[1, 0].plot(ids, [stats.mean(pt[structure].loc[:,'SurfaceArea_left'])- 3*stats.stdev(pt[structure].loc[:,'SurfaceArea_left'])]*len(ids), 'r')
    
    axes[1, 1].scatter(ids,pt[structure].loc[:,'SurfaceArea_right'])
    axes[1, 1].plot(ids, [stats.mean(pt[structure].loc[:,'SurfaceArea_right'])]*len(ids), 'k', label='Mean')
    axes[1, 1].plot(ids, [stats.mean(pt[structure].loc[:,'SurfaceArea_right'])+ 3*stats.stdev(pt[structure].loc[:,'SurfaceArea_right'])]*len(ids), 'r', label='3 SD')
    axes[1, 1].plot(ids, [stats.mean(pt[structure].loc[:,'SurfaceArea_right'])- 3*stats.stdev(pt[structure].loc[:,'SurfaceArea_right'])]*len(ids), 'r')


    figure.gca().legend(loc='center left', bbox_to_anchor=(1, 1.1), ncol=1)


    axes[0, 0].set_title('Left structure part pre-treatment')
    axes[0, 1].set_title('Right structure part pre-treatment')
    axes[1, 0].set_title('Left structure part post-treatment')
    axes[1, 1].set_title('Right structure part post-treatment')
    
    figure.suptitle(structures[structure])
    
    for ax in axes.flat:
        ax.set(xlabel='Participant ID', ylabel='Change (%)')
    for ax in axes.flat:
        ax.label_outer()
        
    plt.show()
        