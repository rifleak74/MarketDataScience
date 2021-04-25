# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:59:13 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
線條Marks圖樣標記
"""
import matplotlib.pyplot as plt
import numpy as np

# Marks
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
x = np.linspace(0, 2, 30)
plt.plot(x, x**3,'-o') #第三個參數設定記號
plt.title('圖片大標題')
plt.xlabel('X資料名稱')
plt.ylabel('Y資料名稱')
plt.xlim(0,2.5)
plt.ylim(0,9)
plt.show()