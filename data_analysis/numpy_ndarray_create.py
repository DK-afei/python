# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:50:12 2020

@author: 0xff
"""

import numpy as np

x = np.array([0,1,2,3])
print(x)

x = np.array((4,5,6,7))
print(x)

x = np.array([[1,2], [9,8], (0.1,0.2)])
print(x)

print()

print(np.arange(10))
print(np.ones((3,6)))
print(np.zeros((3,6), dtype=np.int32))
print(np.eye(5))
y = np.ones((2,3,4))
print(y)
print(y.shape)

print()

a = np.linspace(1,10,4)
print(a)

b = np.linspace(1,10,4, endpoint=False)
print(b)

c = np.concatenate((a,b))
print(c)

