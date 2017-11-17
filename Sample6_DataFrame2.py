# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:15:28 2017

@author: Saicharan.S
"""

import pandas as pd

df = pd.DataFrame({'id':[1,2,3], 'fare':[13, 15.7, 25]})
type(df)
df.shape
df.info()

df['fare']
df.iloc[0:2]