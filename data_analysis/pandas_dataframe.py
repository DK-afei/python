# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:33:38 2020

@author: 0xff
"""

import pandas as pd
import numpy as np

d = pd.DataFrame(np.arange(10).reshape(2,5))
print(d)

dt = {'one':pd.Series([1,2,3], index=['a','b','c']),
      'two':pd.Series([9,8,7,6], index=['a','b','c','d'])}
d = pd.DataFrame(dt)
print(d)
d = pd.DataFrame(dt, index=['b','c','d'], columns=['two','three'])
print(d)

d1 = {'one':[1,2,3,4], 'two':[9,8,7,6]}
d = pd.DataFrame(d1, index=['a','b','c','d'])
print(d)
print(d.index)
print(d.columns)
print(d.values)
print(d['one'])
print(d.ix['a'])
print(d['two']['d'])












