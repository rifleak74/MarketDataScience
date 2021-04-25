# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:03:40 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
輔助標籤文字
"""
import matplotlib.pyplot as plt
import numpy as np

# 輔助標籤文字
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o',label='產品生命線')
plt.grid(True)
plt.text(
    x = 1, # 文字X位置
    y = 1, # 文字Y位置
    s = '重點', # 文字內容
    fontsize = 20, # 大小
    color = '#BF360C', #顏色
    alpha = 0.5, # 透明度
    horizontalalignment='center', # 水平位置
    verticalalignment='center' # 垂直位置
    )
plt.show()