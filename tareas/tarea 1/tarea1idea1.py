# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 08:37:25 2021

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
    
inputs_class = file_clases.distribution_inputs()
inputs_class.data_type = 'real' 
df2=pd.DataFrame(columns=metrics1)

for i in range(size):
   
    inputs_class.variable_name = rics[i]
    dm = file_clases.distribution_manager(inputs_class) 
    dm.load_timeseries() 
    dm.compute()
    
    metrics2 = [rics[i],dm.mean, dm.std, dm.skew, dm.kurtosis, dm.median, dm.var_95,\
           dm.cvar_95, dm.sharpe, dm.jb_stat, dm.p_value, dm.is_normal]
        
    df2.loc[i] = metrics2
    
