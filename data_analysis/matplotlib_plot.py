# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:03:45 2020

@author: 0xff
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(10)
plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, '*', a, a*4.5, 'b-.')
plt.show()