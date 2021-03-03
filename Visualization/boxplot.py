# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:25:57 2020

@author: inger
"""

import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
from statannot import add_stat_annotation


df_ca = pd.read_excel (r'D:\Master_2020\Extracted Features\caudate_all.xlsx')
df_hip = pd.read_excel (r'D:\Master_2020\Extracted Features\hipp_all.xlsx')
df_pal = pd.read_excel (r'D:\Master_2020\Extracted Features\pallidum_all.xlsx')
df_pu = pd.read_excel (r'D:\Master_2020\Extracted Features\putamen_all.xlsx')
df_thal = pd.read_excel (r'D:\Master_2020\Extracted Features\thalamus_all.xlsx')

structures = ['The Caudate', ' The Hippocampus', 'The Pallidum', 'The Putamen', ' The Thalamus']

classes = ['MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH'
           ,'placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo'
           ,'placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo',
           'MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH','MPH'
           ,'placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo'
           ,'placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo','placebo']
Area = ['left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left',
        'left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left','left',
        'left','left','left','left','left','left','right','right','right','right','right','right',
        'right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right',
        'right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right','right']

strucs = [df_ca, df_hip, df_pal, df_pu, df_thal]


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


for structure in range(len(structures)):     
    df_left = pd.DataFrame()
    df_left['Surface Area'] =  strucs[structure].loc[:,'Shape_SurfaceArea_left']
    df_left['Volume'] =  strucs[structure].loc[:,'Shape_MeshVolume_left']
    df_right = pd.DataFrame()
    df_right['Surface Area'] =  strucs[structure].loc[:,'Shape_SurfaceArea_right']
    df_right['Volume'] =  strucs[structure].loc[:,'Shape_MeshVolume_right']

    
    df = pd.DataFrame()
    df = df.append(df_left, ignore_index=True)
    df = df.append(df_right, ignore_index=True)
    df['class'] = classes
    df['Brain half'] = Area
    
    
    f, axes = plt.subplots(1, 2)
        
    h = sns.boxplot(x="Brain half", y="Surface Area", hue="class", data=df, palette="Set1" , ax=axes[0])
    h.legend_.remove()
    h.axes.set_title("Change in surface area after treatment")
    h.set_ylabel("")
    
    add_stat_annotation(h, data=df, x="Brain half", y="Surface Area", hue="class",
                        box_pairs=[(("left", "MPH"), ("left", "placebo")),
                                     (("right", "MPH"), ("right", "placebo"))
                                    ],
                        test='t-test_welch', text_format='star', loc='inside', comparisons_correction=None,
                        line_offset_to_box=0.2, line_offset=0.1, line_height=0.05, text_offset=8,
                        verbose=2)
    
    g = sns.boxplot(x="Brain half", y="Volume", hue="class", data=df, palette="Set1" , ax=axes[1])
    g.legend(loc='center right', bbox_to_anchor=(0.2, -0.1), ncol=2)
    g.axes.set_title("Change in volume after treatment")
    g.set_ylabel("")
    
    add_stat_annotation(g, data=df, x="Brain half", y="Volume", hue="class",
                        box_pairs=[(("left", "MPH"), ("left", "placebo")),
                                     (("right", "MPH"), ("right", "placebo"))
                                    ],
                        test='t-test_welch', text_format='star', loc='inside', comparisons_correction=None,
                        line_offset_to_box=0.2, line_offset=0.1, line_height=0.05, text_offset=8,
                        verbose=2)
    
    f.suptitle(structures[structure])    


#-------------------------------------------------------------------------


        




            

