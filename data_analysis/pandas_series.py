# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:52:11 2020

@author: 0xff
"""

import pandas as pd
import numpy as np
 
a = pd.Series([9,8,7,6], index=['a','b','c','d'])
print(a)

s = pd.Series(25, index=['a','b','c'])
print(s)

d = pd.Series({'a':9, 'b':8, 'c':7}, index=['c','a','b','d'])
print(d)

n = pd.Series(np.arange(5))
print(n)

m = pd.Series(np.arange(5), index=np.arange(9,4,-1))
print(m)

b = pd.Series([9,8,7,6], index=['a','b','c','d'])
print(b)
print(b.index)
print(b.values)
print(type(b.values))

print(b['b'])
print(b[1])
print(b[['c','d',0]])
print(b[['c','d','a']])

print(b[3])
print(b[:3])
print(b[b>b.median()])
print(np.exp(b)) 

print(b['b'])
flag = 'c' in b
print(flag)
flag = 0 in b
print(flag)
print(b.get('f',100))

a = pd.Series([1,2,3],['c','d','e'])
print(a+b)

b.name = 'Series对象'
print(b.name)
b.index.name = '索引列'
print(b)

print(b['a'])
b.name = 'Series'
print(b)
b.name = 'New Series'
b['b','c'] = 20
print(b)
