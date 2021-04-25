# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:55:40 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
網狀線與多線條呈現
"""
import matplotlib.pyplot as plt
import numpy as np

# 多圖重疊
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o') #設定第一條折線圖
plt.plot(x, x**2)  #設定第二條折線圖
plt.plot(x, x**3)  #設定第三條折線圖
plt.title('圖片大標題')
plt.xlabel('X資料名稱')
plt.ylabel('Y資料名稱')
plt.grid(True) # grid 開啟
plt.show()
