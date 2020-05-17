# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:47:06 2020

@author: 0xff
"""

import numpy as np

a = np.array([[0,1,2,3,4],[9,8,7,6,5]])
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)

print()

x = np.array([[0,1,2,3,4],[9,8,7,6]])
print(x.ndim)
print(x.shape)
print(x.size)
print(x.dtype)
print(x.itemsize)