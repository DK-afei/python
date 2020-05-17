# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:54:11 2020

@author: 0xff
"""

import pandas as pd

d1 = {'one':[1,2,3,4], 'two':[9,8,7,6], 'three':[2,8,3,6]}
d = pd.DataFrame(d1, index=['a','b','c','d'])
print(d)

d = d.reindex(columns=['three','two','one'])
print(d)

newc = d.columns.insert(3,'four')
newd = d.reindex(columns=newc, fill_value=2)
print(newd)
print(d.index)
print(d.columns)

d1 = {'one':[1,2,3,4], 'two':[9,8,7,6], 'three':[2,8,3,6]}
d = pd.DataFrame(d1, index=['a','b','c','d'])
print(d)
nc = d.columns.delete(0)
ni = d.index.insert(3,'e')
nd = d.reindex(index=ni, columns=nc).ffill()
print(nd)

a = pd.Series([9,8,7,6], index=['a','b','c','d'])
print(a)
print(a.drop(['b','c']))

d1 = {'one':[1,2,3,4], 'two':[9,8,7,6], 'three':[2,8,3,6]}
d = pd.DataFrame(d1, index=['a','b','c','d'])
print(d)
print(d.drop('a'))
print(d.drop('two',axis=1))







