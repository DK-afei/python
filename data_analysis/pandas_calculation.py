# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:22:28 2020

@author: 0xff
"""
import pandas as pd
import numpy as np

a = pd.DataFrame(np.arange(12).reshape(3,4))
print(a)

b = pd.DataFrame(np.arange(20).reshape(4,5))
print(b)

print(a+b)
print(a*b)

b.add(a, fill_value=100)
a.mul(b, fill_value=0)

c = pd.Series(np.arange(4))
print(c)

print(c-10)
print(b-c)
b.sub(c, axis=0)

d = pd.DataFrame(np.arange(12,0,-1).reshape(3,4))
print(d)

print(a>d)
print(a==d)

print(a>c)
print(c>0)




