# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:01:40 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
圖例
"""
import matplotlib.pyplot as plt
import numpy as np

# 圖例位置
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o',label='蘋果')
plt.plot(x, x**2, label='橘子')
plt.plot(x, x**3, label='香蕉')
plt.title('圖片大標題')
plt.xlabel('X資料名稱')
plt.ylabel('Y資料名稱')
plt.legend(loc =6) #開啟圖例
plt.show()
