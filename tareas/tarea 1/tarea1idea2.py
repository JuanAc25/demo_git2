# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 18:21:19 2021

@author: vicky
"""

#vamos a probar si sirve nuestro codigo

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
metrics1 = ['ric','mean','std','skew','kurtosis','median','var_95','cvar_95',\
            'sharpe','jarque_bera_stat','p_value','is_normal']
metrics2 = ['ric','mean','std','skew'] 

 
inputs_class = file_clases.distribution_inputs()
inputs_class.data_type = 'real' 

c=[]
d=[]
e=[]
f=[]
#for i in metrics2:
    #if i in metrics2:
       # d.append(i)
df2=pd.DataFrame()#columns=d)
for ric in range(size):
   
    inputs_class.variable_name = rics[ric]
    dm = file_clases.distribution_manager(inputs_class) 
    dm.load_timeseries() 
    dm.compute()
    print(dm)
    
    ##e.append(dm.mean)
    f.append(dm.std)
    
    if 'ric' in metrics2 :
       c.append(rics[ric])
       df2['ric']=pd.Series(c)
        
    if 'mean' in metrics2:
        e.append(dm.mean)
        df2['mean']= pd.Series(e)
        
if 'std' in metrics2:
    df2['std']= (f)
   
    if 'skew' in metrics1:
        c.append(dm.skew)
        
