# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:56:25 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
自訂XY刻度
"""
import matplotlib.pyplot as plt
import numpy as np

# 設定刻度
x = np.linspace(0, 2, 30)
plt.plot(x, x**3)
plt.title('圖片大標題')
plt.xlabel('X資料名稱')
plt.ylabel('Y資料名稱')
plt.xlim(0,2.5)
plt.ylim(0,9)
tick_arr = np.arange(0,2.5,0.2) #產生刻度陣列(npArray 類似list)
plt.xticks(tick_arr) # 設定刻度
plt.yticks([]) # 空值代表隱藏刻度
plt.show()