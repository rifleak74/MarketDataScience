# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:29:03 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第六章Matplotlib繪圖
基本繪圖－XY資料、折線、直方、圓餅、點陣圖
"""
import matplotlib.pyplot as plt
import pandas as pd 

# 加入XY資料
x = [1, 2, 3, 4]
y = [4, 8, 12, 16]
plt.plot(x, y) # 放入XY資料
plt.show()


# pandas資料繪圖
data = pd.DataFrame([
    {'a':1,'b':3},
    {'a':2,'b':4}])
data
plt.plot(data) # 放入pandas資料
plt.show()


# 棒狀圖
names = ['蘋果', '橘子', '檸檬', '芭樂']
values = [10, 56 ,5 ,20]
plt.bar(names, # X資料
        values, # Y資料
        0.5, # bar寬度
        color='#7CA5B8' # bar顏色
        )
plt.show()


# 散佈圖
plt.scatter(
    [1,2,3,4,2,3,4,3,5,5], # X值
    [5,5,6,7,10,2,7,10,8,5], # Y值
    s = [70,20,100,20,30,50,30,50,60,70], # 圓圈size
    c = [1,2,3,4,1,2,3,4,1,2] # 圓圈color
    )
plt.show()


# 圓餅圖
plt.pie(
        [15, 30, 45, 10], # 各數值比例
        explode = [0.3, 0.1, 0, 0] , # 圓餅散開程度
        labels = ['蘋果', '香蕉', '橘子', '西瓜'], # 標籤
        autopct = '%1.1f%%', # 數值格式
        shadow = True, # 陰影
        startangle = 90 # 轉向角度
        )
# 讓圓餅圖畫出來是圓形
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html
plt.axis('tight')  
plt.show()

