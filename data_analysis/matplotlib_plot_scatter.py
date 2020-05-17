# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:37:18 2020

@author: 0xff
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Simple Scatter')

plt.show()