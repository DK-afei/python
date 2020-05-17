# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:05:22 2020

@author: 0xff
"""

import numpy as np

a = np.ones((2,3,4), dtype=np.int32)

print(a.reshape((3,8)))
print(a)

a.resize((3,8))
print(a)

a = np.ones((2,3,4), dtype=np.int32)
print(a.flatten())
print(a)
b = a.flatten()
print(b)

print()

a = np.ones((2,3,4), dtype=np.int)
print(a)
b = a.astype(np.float)
print(b)

print()

a = np.full((2,3,4), 25, dtype=np.int32)
print(a)
print(a.tolist())