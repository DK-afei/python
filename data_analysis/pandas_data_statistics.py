# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:23:35 2020

@author: 0xff
"""
import pandas as pd
import numpy as np

a = pd.Series([9,8,7,6], index=['a','b','c','d'])
print(a)

print(a.describe())

print(type(a.describe()))

print(a.describe()['count'])
print(a.describe()['max'])

b = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
print(b)
print(b.describe())

print(type(b.describe()))
print(b.describe().ix['max'])
print(b.describe()[2])















