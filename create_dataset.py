# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:14:11 2020

@author: inger
"""
import pandas as pd


def concat_mph_plac(data_mph, data_plac):
    if type(data_mph)==str:
        df_mph = pd.read_csv(data_mph)
        df_plac = pd.read_csv(data_plac)
        
        if 'Unnamed: 0' in df_mph.columns:
            df_mph = df_mph.drop(columns = ['Unnamed: 0'])
        if 'Unnamed: 0' in df_plac.columns:
            df_plac = df_plac.drop(columns = ['Unnamed: 0'])
        if 'Name' in df_mph.columns:
            df_mph = df_mph.drop(columns = ['Name'])
        if 'Name' in df_plac.columns:
            df_plac = df_plac.drop(columns = ['Name'])
         
        if 'Label' not in df_mph.columns:
            df_mph.insert(loc = 0, column = 'Label', value = [1]*len(df_mph.index))
        if 'Label' not in df_plac.columns:
            df_plac.insert(loc = 0, column = 'Label', value = [0]*len(df_plac.index))
    
        df = pd.concat([df_mph, df_plac], ignore_index=True)
        
    else: 
        df = pd.merge(data_mph, data_plac, right_index=True, left_index=True, suffixes=('_left', '_right'))
        df = df.drop('Label_right', axis=1)
        df  = df.rename(columns={'Label_left':'Label'})
        
    return df

def concat_left_right(left, right):
    if type(left)==str:
        df_left = pd.read_csv(left)
        df_right = pd.read_csv(right)
        
        if 'Unnamed: 0' in df_left.columns:
            df_left = df_left.drop(columns = ['Unnamed: 0'])
        if 'Unnamed: 0' in df_right.columns:
            df_right = df_right.drop(columns = ['Unnamed: 0'])
        if 'Name' in df_left.columns:
            df_left = df_left.drop(columns = ['Name'])
        if 'Name' in df_right.columns:
            df_right = df_right.drop(columns = ['Name'])
         
        if 'Label' not in df_left.columns:
            df_left.insert(loc = 0, column = 'Label', value = [1]*len(df_left.index))
        if 'Label' not in df_right.columns:
            df_right.insert(loc = 0, column = 'Label', value = [0]*len(df_right.index))
    
        df = pd.concat([df_left, df_right], axis=1)
        
    else: 
        df = pd.merge(left, right, right_index=True, left_index=True, suffixes=('_left', '_right'))
        df = df.drop('Label_right', axis=1)
        df  = df.rename(columns={'Label_left':'Label'})
    
    return df
    
def difference(bl, pt):
    
    shape1 = bl.shape
    diff = pd.DataFrame(data=([0]*shape1[1],)*shape1[0], columns=bl.columns)
    diff.iloc[:,0] = bl.iloc[:,0]
    
    if 'Label' in bl.columns:
        for row in range(0, shape1[0]):
            for col in range(1, shape1[1]):
                diff.iloc[row, col] = pt.iloc[row,col]-bl.iloc[row, col]
    else:
        for row in range(shape1[0]):
            for col in range(shape1[1]):
                diff.iloc[row, col] = pt.iloc[row,col]-bl.iloc[row, col]
                
    return diff




def concat_striatum(caudate, pallidum, putamen):
    caudate_df = pd.read_csv(caudate)
    pallidum_df = pd.read_csv(pallidum)
    putamen_df = pd.read_csv(putamen)
    
    ca={}
    for ind in range(len(caudate_df.columns)):
        ca[caudate_df.columns[ind]] = caudate_df.columns[ind] + '_ca'
    caudate_df = caudate_df.rename(columns=ca)
    
    pa={}
    for ind in range(len(pallidum_df.columns)):
        pa[pallidum_df.columns[ind]] = pallidum_df.columns[ind] + '_pa'
    pallidum_df = pallidum_df.rename(columns=pa)

    pu={}
    for ind in range(len(putamen_df.columns)):
        pu[putamen_df.columns[ind]] = putamen_df.columns[ind] + '_pu'
    putamen_df = putamen_df.rename(columns=pu)    
    
        
    dfs = [caudate_df, pallidum_df, putamen_df]
    result = pd.concat(dfs, axis=1, sort=False)
    result = result.drop(columns=['Unnamed: 0_ca', 'Unnamed: 0_pa', 'Unnamed: 0_pu', 'Label_pa', 'Label_pu'])
    result = result.rename(columns={'Label_ca':'Label'})

    return result

        
if __name__== "__main__":
    texture_list = ['\GRSZM', '\GLRLM', '\GLDM']
    brain = ['\caudate', '\hippocampus', '\pallidum', '\putamen', '\\thalamus']
    
    for texture in texture_list:
        for structure in brain:     
            mph_bl_left= r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+'\single' +structure+ '_left_mph_bl.csv'
            mph_bl_right= r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+'\single' +structure+ '_right_mph_bl.csv'
            
            plac_bl_left = r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+'\single' +structure+ '_left_placebo_bl.csv'
            plac_bl_right = r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+'\single' +structure+ '_right_placebo_bl.csv'
            
            mph_pt_left= r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+'\single' +structure+ '_left_mph_pt.csv'
            mph_pt_right= r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+'\single' +structure+ '_right_mph_pt.csv'
            
            plac_pt_left = r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+'\single' +structure+ '_left_placebo_pt.csv'
            plac_pt_right = r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+'\single' +structure+ '_right_placebo_pt.csv'
            
           
            #BL: concat MPH and placebo groups
            left_bl = concat_mph_plac(mph_bl_left, plac_bl_left)
            right_bl = concat_mph_plac(mph_bl_right, plac_bl_right)
            
            #BL: concat left and right
            bl = concat_left_right(left_bl, right_bl)
            bl.to_csv(r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+structure+'_texture_norm_children_bl.csv')
            
            #PT: concat MPH and placebo groups
            left_pt = concat_mph_plac(mph_pt_left, plac_pt_left)
            right_pt = concat_mph_plac(mph_pt_right, plac_pt_right)
            
            #PT: concat left and right
            pt = concat_left_right(left_pt, right_pt)
            pt.to_csv(r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+structure+'_texture_norm_children_pt.csv')
            
            #the difference
            data = difference(bl, pt)
            data.to_csv(r'D:\Master_2020\Extracted Features\texture_after_autoscale_children\64'+texture+structure+'_texture_norm_children__diff.csv')
    
        