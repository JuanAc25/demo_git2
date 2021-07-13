# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:37:22 2021

@author: vicky
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

import file_clases
importlib.reload(file_clases)

rics=['BARC.L','BBVA.MC','BNP.PA']
size = len(rics)

#metrics1 = ['ric','mean','p_value','is_normal']
metrics1 = ['ric','mean','std','skew','kurtosis','median','var_95','cvar_95',\
            'sharpe','jarque_bera_stat','p_value','is_normal']
#metrics1 = ['ric','std','skew','kurtosis','var_95','cvar_95']
inputs_class = file_clases.distribution_inputs()
inputs_class.data_type = 'real' 

c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
k=[]
l=[]
m=[]
n=[]

df2=pd.DataFrame()
for ric in range(size):
   
    inputs_class.variable_name = rics[ric]
    dm = file_clases.distribution_manager(inputs_class) 
    dm.load_timeseries() 
    dm.compute()
    print(dm)
    c.append(rics[ric])
    d.append(dm.mean)
    e.append(dm.std)
    f.append(dm.skew)
    g.append(dm.kurtosis)
    h.append(dm.median)
    i.append(dm.var_95)
    j.append(dm.cvar_95)
    k.append(dm.sharpe)
    l.append(dm.jb_stat)
    m.append(dm.p_value)
    n.append(dm.is_normal)
    
if 'ric' in metrics1 :
    df2['ric']= pd.Series(c)       
if 'mean' in metrics1:
    df2['mean']= pd.Series(d)      
if 'std' in metrics1:
    df2['std']= (e)
if 'skew' in metrics1:
     df2['skew']= (f)
if 'kurtosis' in metrics1:
     df2['kurtosis']= (g)
if 'median' in metrics1:
     df2['median']= (h)
if 'skew' in metrics1:
     df2['var_95']= (i)
if 'cvar_95' in metrics1:
     df2['cvar_95']= (j)
if 'sharpe' in metrics1:
     df2['sharpe']= (k)
if 'jarque_bera_stat' in metrics1:
     df2['jarque_bera_stat']= (l)
if 'p_value' in metrics1:
     df2['p_value']= (m)
if 'is_normal' in metrics1:
     df2['is_normal']= (n)