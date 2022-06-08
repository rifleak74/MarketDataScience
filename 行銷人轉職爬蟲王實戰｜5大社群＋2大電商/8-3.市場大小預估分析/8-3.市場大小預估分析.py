# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:53:32 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第八章 shapee市場預估－這個市場有多大？
市場大小預估分析
"""
from tqdm import tqdm
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
colors = ['#d9f776','#76f794','#9476f7','#f776d9','#e70e4b','#76d9f7','#f79476','#fbccbe','#befbcc','#fbbeed']
getdata = pd.read_csv('花襯衫_商品資料.csv', encoding='utf-8')
getdata.columns

#--- 若沒有tag，則從文章中整理出Tag
containar = []
for i in range(len(getdata)):
    getArticle = getdata['商品文案'][i] #抓取每篇文案
    
    getArticle = getArticle.replace('＃','#') # 半形全形一致
    item = []
    for j in getArticle.split('#'): # 利用「#」來做切割
        if len(j) < 10 : # 若tag大於10個字則不計入
            j = j.replace(' ','') # 取代空白
            j = j.replace('^n','') # 取代^n
            if len(j) >0 : # 要確認取代完成後還有剩下東西
                item.append(j)
    containar.append(item)

getdata['Tag'] = containar

#--- 整理成可以被Kmean分析的資料
KmeansData = getdata[['商品ID','價格','歷史銷售量','Tag']]

allpro = KmeansData['Tag'].sum()
allpro = pd.DataFrame(allpro)
allpro.dropna(inplace=True)

KmeansData['Tag'] = KmeansData['Tag'].astype(str)
count=0
for i in tqdm(allpro[0].value_counts().index):
    KmeansData['c'+str(count)] = np.where(KmeansData['Tag'].str.contains(i),1,0)
    count = count+1
    
#--- 開始分類
crub = 10 #總共要分成幾群
clf = KMeans(n_clusters=crub)
clf.fit(KmeansData[['c'+str(x) for x in range(count)]].values.tolist())#開始訓練

#--- 取得預測結果
getdata['類群'] = clf.labels_

#--- Kmean分類圖
for i in range(crub):
    draw = getdata[getdata['類群']==i]
    print('第' + str(i) + '群數量：　' + str(len(draw)))
    plt.scatter(draw['價格'],draw['歷史銷售量'], 
                color=colors[i], 
                label = i,
                alpha=0.5)
plt.title("Kmean分類圖",fontsize=30)#標題
plt.xlabel("價格",fontsize=15)#y的標題
plt.ylabel("歷史銷售量",fontsize=15) #x的標題
plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2) # 設置圖例
plt.grid(True) # grid 開啟
plt.tight_layout()

#--- 各群tag top 20
for i in range(10):
    draw = getdata[getdata['類群']==i]
    draw = pd.DataFrame(draw['Tag'].sum())[0].value_counts()
    
    plt.bar(draw.index[0:20],
            draw[0:20].values, 
                color='#d9f776',
                alpha=0.5)
    plt.xticks(rotation=70)
    plt.title("第"+str(i)+"群tag的top20",fontsize=30)#標題
    plt.xlabel("tag名稱",fontsize=15)#y的標題
    plt.ylabel("數量",fontsize=15) #x的標題

    plt.tight_layout()
    plt.savefig("第"+str(i)+"群tag的top20.png", dpi=300) # 存檔且設定解析度
    plt.close()
    
#--- 各群的總市值
getdata['總收入'] = getdata['價格'] * getdata['歷史銷售量']
for i in range(10):
    draw = getdata[getdata['類群']==i]
    print('第'+str(i)+'群總收入： '+str(draw['總收入'].sum()))