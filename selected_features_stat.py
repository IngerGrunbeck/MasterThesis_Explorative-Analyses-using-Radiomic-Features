# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:35:07 2020

@author: inger

This script creates piecharts showing the fraction of each feature-category selected by the the feature selection algorithms. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


SMALL_SIZE = 24
MEDIUM_SIZE = 46
BIGGER_SIZE = 52

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title

struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_caudate\features_freq_20200610-144901.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

freq = pd.DataFrame(columns=['Features', 'Selection rate', 'Type'])
freq['Features']=struc_freq.iloc[:5,0]
freq['Selection rate']=struc_freq.iloc[:5, 1]
ax_bar = freq.plot.barh(x='Features', y='Selection rate', legend=False, )

plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    right=False,
    left=False)         # ticks along the top edge are off
plt.show()


struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_hippocampus\features_freq_20200610-150915.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

freq = pd.DataFrame(columns=['Features', 'Selection rate', 'Type'])
freq['Features']=struc_freq.iloc[:5,0]
freq['Selection rate']=struc_freq.iloc[:5, 1]
ax_bar = freq.plot.barh(x='Features', y='Selection rate', legend=False, )

plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    right=False,
    left=False)         # ticks along the top edge are off
plt.show()


struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_pallidum\features_freq_20200610-145854.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

freq = pd.DataFrame(columns=['Features', 'Selection rate', 'Type'])
freq['Features']=struc_freq.iloc[:5,0]
freq['Selection rate']=struc_freq.iloc[:5, 1]
ax_bar = freq.plot.barh(x='Features', y='Selection rate', legend=False, )

plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    right=False,
    left=False)         # ticks along the top edge are off
plt.show()


struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_putamen\features_freq_20200610-151939.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

freq = pd.DataFrame(columns=['Features', 'Selection rate', 'Type'])
freq['Features']=struc_freq.iloc[:5,0]
freq['Selection rate']=struc_freq.iloc[:5, 1]
ax_bar = freq.plot.barh(x='Features', y='Selection rate', legend=False, )

plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    right=False,
    left=False)         # ticks along the top edge are off
plt.show()


struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\left_right\thalamus_all\features_freq_20200603-194857.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

freq = pd.DataFrame(columns=['Features', 'Selection rate', 'Type'])
freq['Features']=struc_freq.iloc[:5,0]
freq['Selection rate']=struc_freq.iloc[:5, 1]
ax_bar = freq.plot.barh(x='Features', y='Selection rate', legend=False, )

plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    right=False,
    left=False)         # ticks along the top edge are off
plt.show()


SMALL_SIZE = 16
MEDIUM_SIZE =12
BIGGER_SIZE = 16

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title

#caudate
struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_caudate\features_freq_20200610-144901.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()

struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_caudate\features_freq_20200610-144901.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1*struc_freq.iloc[item, 1]
        
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()

#hippocampus
struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_hippocampus\features_freq_20200610-150915.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1
        
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()


struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_hippocampus\features_freq_20200610-150915.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1*struc_freq.iloc[item, 1]
        
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()

#pallidum
struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_pallidum\features_freq_20200610-145854.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1
        
        
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()


struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_pallidum\features_freq_20200610-145854.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1*struc_freq.iloc[item, 1]
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()


#putamen
struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_putamen\features_freq_20200610-151939.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1
        
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()

struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_putamen\features_freq_20200610-151939.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1*struc_freq.iloc[item, 1]
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()

#thalamus
struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_thalamus\features_freq_20200610-152953.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1
        
        
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()

struc_freq = pd.read_csv(r'C:\Users\inger\Desktop\Thesis\Ahmed res\mean\full_mean_thalamus\features_freq_20200610-152953.csv', header=None)
struc_freq.iloc[:,1] = struc_freq.iloc[:,1]/24

bin64_texture = 0
bin128_texture = 0
shape = 0
for item in range(len(struc_freq)):
    if struc_freq.iloc[item, 0][:2] == '64':
        bin64_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:3] == '128':
        bin128_texture += 1*struc_freq.iloc[item, 1]
    if struc_freq.iloc[item, 0][:5] == 'Shape':
        shape += 1*struc_freq.iloc[item, 1]
        
labels = '64-bin texture', ' 128-bin texture', 'shape'
Selection_rate = [bin64_texture, bin128_texture, shape]

fig1 , ax1 = plt.subplots()
ax1.pie(Selection_rate, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.show()





