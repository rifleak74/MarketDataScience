# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:02:51 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
輔助線
"""
import matplotlib.pyplot as plt
import numpy as np

# 輔助線
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o',label='蘋果')
plt.plot(x, x**2, label='香蕉')
plt.plot(x, x**3, label='橘子')
plt.axhline( # 繪製平均線，axvline
    2, # y位置
    color='#33CCFF', # 線條顏色 
    linestyle='dashed', # 線條樣式
    linewidth=1 # 線條粗度
    ) 
plt.show()