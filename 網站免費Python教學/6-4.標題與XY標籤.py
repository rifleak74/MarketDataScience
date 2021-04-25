# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:29:03 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
標題與XY標籤
"""
import matplotlib.pyplot as plt
import numpy as np

# 加上標題與XY標籤
x = np.linspace(0, 5, 30) # 產生0～5的連續資料
plt.plot(x, x**3)
plt.title('圖片大標題', fontsize = 30) #加入標題
plt.xlabel('X資料名稱') #加x軸標籤
plt.ylabel('Y資料名稱') #加y軸標籤
plt.show()