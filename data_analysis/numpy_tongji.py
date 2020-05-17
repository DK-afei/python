# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:43:40 2020

@author: 0xff
"""

import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print(np.sum(a))
print(np.mean(a, axis=1))
print(np.mean(a, axis=0))
print(np.average(a, axis=0, weights=[10,5,1]))
print(np.std(a))
print(np.var(a))

print()

b = np.arange(15,0,-1).reshape(3,5)
print(b)
print(np.max(b))
print(np.argmax(b))
print(np.unravel_index(np.argmax(b), b.shape))
print(np.ptp(b))
print(np.median(b))


