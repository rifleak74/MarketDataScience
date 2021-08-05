# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:36:03 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
FoodPanda熱門美食系列
"""
import matplotlib.pyplot as plt
import pandas as pd 
import jieba
import jieba.analyse

getdata = pd.read_csv('foodpanda.csv', encoding = 'utf-8')
getdata.columns
text = getdata['標籤'].sum()

keywords1=jieba.analyse.extract_tags(text)
print("/".join(keywords1))

# top 3 關鍵字
keywords_top=jieba.analyse.extract_tags(text,
                                        topK=10, 
                                        withWeight=True)
keywords_top = pd.DataFrame(keywords_top)
# 棒狀圖
plt.bar(keywords_top[0], # X資料
        keywords_top[1], # Y資料
        0.5, # bar寬度
        color='#EF798A' # bar顏色
        )
plt.title('美食系列排名', fontsize = 30) #加入標題
plt.xlabel('美食系列') #加x軸標籤
plt.ylabel('分數') #加y軸標籤
plt.xticks(rotation=30)
plt.show()