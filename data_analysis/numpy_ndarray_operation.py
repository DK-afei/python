# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:13:36 2020

@author: 0xff
"""

import numpy as np

a = np.array([9,8,7,6,5])
print(a[2])
print(a[1:4:2])

print()

a = np.arange(24).reshape((2,3,4))
print(a)
print(a[1,2,3])
print(a[0,1,2])
print(a[-1,-2,-3])
print()
print(a[:,1,-3])
print(a[:,1:3,:])
print(a[:,:,::2])
