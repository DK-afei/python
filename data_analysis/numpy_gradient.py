# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:48:34 2020

@author: 0xff
"""

import numpy as np

a = np.random.randint(0,20,(5))
print(a)
print(np.gradient(a))
b = np.random.randint(0,20,(5))
print(b)
print(np.gradient(b))


print()
c = np.random.randint(0,50,(3,5))
print(c)
print(np.gradient(c))



