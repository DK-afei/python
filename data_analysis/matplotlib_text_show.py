# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:27:22 2020

@author: 0xff
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2*np.pi*a), 'r--')

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=25, color='green')
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=25)
plt.title(r'正弦波实例$y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
#plt.text(2,1, r'$\mu=100$', fontsize=15)
plt.annotate(r'$\mu=100$', xy=(2,1), xytext=(3, 1.5), 
             arrowprops=dict(facecolor='black', shrink=0.1, width=2))

plt.axis([-1,6,-2,2])
plt.grid(True)
plt.show