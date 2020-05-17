# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:42:32 2020

@author: 0xff
"""

import pandas as pd
import numpy as np

b = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
print(b)

print(b.cumsum())
print(b.cumprod())
print(b.cummin())
print(b.cummax())

print(b.rolling(2).sum())
print(b.rolling(3).sum())


#相关性计算
hprice = pd.Series([3.04,22.93,12.75,22.6,12.33],index=['2008','2009','2010','2011','2012'])
m2 = pd.Series([8.18,18.38,9.13,7.82,6.69],index=['2008','2009','2010','2011','2012'])

print(hprice.corr(m2))









