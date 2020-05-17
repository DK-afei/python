# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:16:46 2020

@author: 0xff
"""

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib

#全局设置
#matplotlib.rcParams['font.family']='STSong'
#matplotlib.rcParams['font.size']=20

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间',fontproperties='SimHei', fontsize=20)
plt.ylabel('纵轴：振幅',fontproperties='SimHei', fontsize=20)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()