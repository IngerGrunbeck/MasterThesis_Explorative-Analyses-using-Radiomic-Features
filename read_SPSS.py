# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:03:26 2020

__author__ = 'Inger Annett Grünbeck'
__email__ = 'inger.gruenbeck@gmail.com'
"""

import pandas as pd


df = pd.read_spss('D:/Master_2020/Data/CGI_cecilia.sav')
cgi = df.loc[:, ['PTn', 'MED_GROUP', 'AGE', 'AGE_GROUP', 'CGI_CHANGE_PT']]

df1 = cgi.dropna(axis=0)
df_kids = df1.loc[:49,:]
df_adult = df1.loc[50:,:]

df_kids_mph = df_kids[df_kids['MED_GROUP'] == 'MPH']
df_kids_plac = df_kids[df_kids['MED_GROUP'] == 'PLACEBO']
df_ad_mph = df_adult[df_adult['MED_GROUP'] == 'MPH']
df_ad_plac = df_adult[df_adult['MED_GROUP'] == 'PLACEBO']


print('---kids with MPH---')
df_kids_mph.plot.hist(y='CGI_CHANGE_PT')
print('---kids with placebo---')
df_kids_plac.plot.hist(y='CGI_CHANGE_PT')
print('---adults with MPH---')
df_ad_mph.plot.hist(y='CGI_CHANGE_PT')
print('---adults with placebo---')
df_ad_plac.plot.hist(y='CGI_CHANGE_PT')