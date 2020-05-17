# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:00:00 2020

@author: 0xff
"""

import pandas as pd
import numpy as np

b = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
print(b)

print(b.sort_index())
print(b.sort_index(ascending=False))

c = b.sort_index(axis=1, ascending=False)
print(c)
print(c.sort_index())

d = b.sort_values(2, ascending=False)
print(d)
d = c.sort_values('a',axis=1, ascending=False)
print(d)

a = pd.DataFrame(np.arange(12).reshape(3,4), index=['a','b','c'])
print(a)
b = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
print(b)

c = a+b
print(c)
print(c.sort_values(2, ascending=False))
print(c.sort_values(2, ascending=True))












