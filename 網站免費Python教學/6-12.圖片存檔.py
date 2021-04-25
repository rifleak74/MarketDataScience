# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:04:28 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
圖片存檔
"""
import matplotlib.pyplot as plt
import numpy as np

# 圖片存檔
x = np.linspace(0, 2, 30)
plt.plot(x, x, '-o',label='產品生命線')
plt.title('圖片大標題')
plt.xlabel('X資料名稱')
plt.ylabel('Y資料名稱')
#切記，必須在show之前先save
plt.savefig('存檔名稱.png', dpi=300) # 存檔且設定解析度
plt.show()