# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:53:20 2020

@author: inger
"""


import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
from statannot import add_stat_annotation


df_hip = pd.read_excel (r'D:\Master_2020\Extracted Features\hipp_all.xlsx')
df_pal = pd.read_excel (r'D:\Master_2020\Extracted Features\pallidum_all.xlsx')
df_pu = pd.read_excel (r'D:\Master_2020\Extracted Features\putamen_all.xlsx')
df_thal = pd.read_excel (r'D:\Master_2020\Extracted Features\thalamus_all.xlsx')
dfs = [df_hip, df_pal, df_pu, df_thal]
na = ['hippocampus', 'pallidum', 'putamen', 'thalamus']
count = 0
for df in dfs:
    
    df_new = pd.DataFrame(columns=df.columns)
    df_new['ID'] = df['ID']
    df_new['Label'] = df['Label']
    
    #shape
    for name in range(2,16):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+14])/2
    df_new = df_new.drop(columns=df_new.columns[16:30])
    
    #texture 1
    for name in range(16, 40):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+24])/2
    df_new = df_new.drop(columns=df_new.columns[40:64])
    
    for name in range(40, 45):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+5])/2
    df_new = df_new.drop(columns=df_new.columns[45:50])
    
    for name in range(45, 61):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+16])/2
    df_new = df_new.drop(columns=df_new.columns[61:77])
    
    
    for name in range(61, 77):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+16])/2
    df_new = df_new.drop(columns=df_new.columns[77:93])
    
    for name in range(77, 91):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+14])/2
    df_new = df_new.drop(columns=df_new.columns[91:105])
    
    
    
    #texture 2
    
    for name in range(91, 115):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+24])/2
    df_new = df_new.drop(columns=df_new.columns[115:139])
    
    for name in range(115,120):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+5])/2
    df_new = df_new.drop(columns=df_new.columns[120:125])
    
    for name in range(120, 136):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+16])/2
    df_new = df_new.drop(columns=df_new.columns[136:152])
    
    
    for name in range(136, 152):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+16])/2
    df_new = df_new.drop(columns=df_new.columns[152:168])
    
    for name in range(152, 166):
        if df_new.columns[name][:-5]=='_left':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-5]})
        if df_new.columns[name][:-7]=='_left.1':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
        if df_new.columns[name][:-7]=='_left.2':
            df_new = df_new.rename(columns={df_new.columns[name]:df_new.columns[name][:-7]})
            
        df_new.iloc[:, name] = (df.iloc[:,name]+df.iloc[:,name+14])/2
    df_new = df_new.drop(columns=df_new.columns[166:180])
    
    
    
    df_new.to_csv('full_mean_'+na[count]+'.csv', index=False)
    
    count += 1