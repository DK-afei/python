# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:26:29 2020

@author: 0xff
"""

import numpy as np

a = np.random.rand(3,4,5)
print(a)

print()

sn = np.random.randn(3,4,5)
print(sn)

print()

b = np.random.randint(100,200, (3,4))
print(b)
np.random.seed(10)
print(np.random.randint(100,200,(3,4)))
np.random.seed(10)
print(np.random.randint(100,200,(3,4)))

print()

a = np.random.randint(100,200,(3,4))
print(a)
np.random.shuffle(a)
print(a)
np.random.shuffle(a)
print(a)

print()

a = np.random.randint(100,200,(3,4))
print(a)
print(np.random.permutation(a))
print(a)

print()

b = np.random.randint(100,200,(8,))
print(b)
print(np.random.choice(b,(3,2)))
print(np.random.choice(b,(3,2),replace=False))
print(np.random.choice(b,(3,2),p=b/np.sum(b)))

print()

u = np.random.uniform(0,10,(3,4))
print(u)
n = np.random.normal(10,5,(3,4))
print(n)








