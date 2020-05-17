# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:18:27 2020

@author: 0xff
"""

import numpy as np

a = np.arange(24).reshape((2,3,4))
print(a)

print()

print(a.mean())
a = a / a.mean()
print(a)

print()

a = np.arange(24).reshape((2,3,4))
print(a)

print(np.square(a))
a = np.sqrt(a)
print(a)
print(np.modf(a))


print()
a = np.arange(24).reshape((2,3,4))
b = np.sqrt(a)
print(a)
print(b)
print(np.maximum(a,b))
print(a>b)

