#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:58:46 2020

@author: ivan
"""

import jieba.analyse
import pandas as pd
import jieba
import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
jieba.set_dictionary('dict.txt.big')
colrogroup = ['#427f8f','#4a8fa1','#559db0','#66a7b8','#77b1c0','#89bbc8','#9ac5d0','#bdd9e0','#cee3e8','#e0edf0']
colrogroup2 = ['#cd0003','#e60003','#ff0004','#ff1a1d','#ff3436','#ff4d4f','#ff6768','#ff8181','#ff9a9b','#ffb4b4']
# 無意義字元列表，可以自行新增
removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel',
              'nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
              'goo.gl','f2','email','map','f1','f6','__cf___','data','bbs'
              'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
              '標題','時間','看板','<','>','，','。','？','-','閒聊','・','/',
              ' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
              ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》','_'
              ,'.','、','（','）',' ','*','※','~','○','"','"','～','@','＋','\r'
              ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝'
              ,'\l']
#設定你關心的影劇名稱
movie = ['成為王的男人','皇后的品格','赤月青日','神的測驗','死之詠讚',
         '加油吧威基基','皮諾丘','魔女寶鑑','男朋友','來自星星的你']
# 讀入爬蟲資料
KoreaDrama=pd.read_csv('KoreaDrama_re.csv',encoding='utf-8',engine='python',error_bad_lines=False) #開啟檔案

#所有文章和標題都串在一起
thearticle = KoreaDrama['標題'] + KoreaDrama['內容']
#所有文章和標題都串在一起
theSTR = KoreaDrama['標題'].sum() + KoreaDrama['內容'].sum()
  
s = SnowNLP(theSTR)

# 移除無意義字元列
for word in removeword:
    thearticle = thearticle.replace(word,'')


tatal_movie = []
tatal_NLP = []
for mov in movie:
    count = 0
    tatal_sentence = 0
    for art in thearticle:
        if mov in art:
            count = count +1
    tatal_movie.append(count)
    
    for sentence in s.sentences:
        if mov in sentence:
            tatal_sentence = tatal_sentence +SnowNLP(sentence).sentiments

    tatal_NLP.append(tatal_sentence)



    


plt.figure(figsize=(20,10))
# 繪製圓點
plt.scatter(tatal_NLP,tatal_movie, color=colrogroup2, s=3000, alpha=0.5)
# 加上文字註解
for i in range(len(movie)):
    plt.text(tatal_NLP[i],tatal_movie[i], movie[i], fontsize=15 )

plt.plot(np.arange(0, 15, 0.5), color='c', linestyle='dashed', linewidth=1) # 繪製線
plt.grid(True)
plt.title("品牌口碑輿情分析圖",fontsize=30)#標題
plt.ylabel('聲量', fontsize=20)#y的標題
plt.xlabel('正評價', fontsize=20) #x的標題
#plt.savefig('品牌口碑輿情分析圖'+'.png', dpi=300)
plt.show()