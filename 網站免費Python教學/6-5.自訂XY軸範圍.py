# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:29:03 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
自訂XY軸範圍
"""
import matplotlib.pyplot as plt
import numpy as np

# 設定軸範圍
x = np.linspace(0, 2, 30)
plt.plot(x, x**3)
plt.title('圖片大標題')
plt.xlabel('X資料名稱')
plt.ylabel('Y資料名稱')
plt.xlim(0,2.5) #設定x軸顯示範圍
plt.ylim(0,9) #設定y軸顯示範圍
plt.show()