# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:59:19 2022

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第四章 Dcard爆點分析
爆點分析
"""
import datetime
import matplotlib.pyplot as plt
import pandas as pd
# 色碼表
colors = ['#f44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3',
          '#03A9F4', '#00BCD4', '#009688', '#4CAF50', '#8BC34A', '#CDDC39',
          '#FFEB3B', '#FFC107', '#FF9800', '#FF5722', '#795548', '#9E9E9E',
          '#607D8B', '#212121']
# 資料來自talk版
dcard_article = pd.read_csv('Dcard文章資料.csv')
dcard_comment = pd.read_csv('Dcard留言資料.csv')
dcard_article.columns
dcard_comment.columns

#--- 先行填滿空值
dcard_article['標題'] = dcard_article['標題'].fillna('')
dcard_article['內文簡介'] = dcard_article['內文簡介'].fillna('')
dcard_article['主題標籤'] = dcard_article['主題標籤'].fillna('')
dcard_comment['留言內容'] = dcard_comment['留言內容'].fillna('')

# 時間轉換
dcard_article['發文時間'] = pd.to_datetime(dcard_article['發文時間'])
dcard_comment['發文時間'] = pd.to_datetime(dcard_comment['發文時間'])

if dcard_article['發文時間'].min() < dcard_comment['發文時間'].min():
    firsttime = dcard_article['發文時間'].min()
else:
    firsttime = dcard_comment['發文時間'].min()


def evaluation(thestr):
    return eval(thestr)  # 轉換str中的內容真正型態


dcard_article['主題標籤'] = dcard_article['主題標籤'].apply(
    evaluation)  # 將dataframe的資料內容套入方法
alltag = dcard_article['主題標籤'].sum()  # 將所有tag串再一起
alltag = pd.DataFrame(alltag)
alltag.dropna(inplace=True)  # 刪除空值
alltag.drop_duplicates(0, inplace=True)

thetime = []
remember = []
doit = True
while doit:
    firsttime = firsttime + datetime.timedelta(hours=1)
    print(firsttime)

    getdata_article = dcard_article[dcard_article['發文時間'] < firsttime]
    getdata_comment = dcard_comment[dcard_comment['發文時間'] < firsttime]
    if len(getdata_article) == len(dcard_article) and len(getdata_comment) == len(getdata_comment):
        doit = False

    else:
        thetime.append(firsttime)
        allstr = getdata_article['標題'].sum() + getdata_article['內文簡介'].sum(
        ) + getdata_article['主題標籤'].astype(str).sum() + getdata_comment['留言內容'].sum()
        temp = []
        for i in alltag[0]:
            temp.append(allstr.count(i))
        remember.append(temp)

timeflow = pd.DataFrame(remember)
timeflow.columns = alltag[0]


count = 0
for i in timeflow.columns:
    plt.plot(thetime, timeflow[i],
             color=colors[count % 20],
             linewidth=5,
             alpha=0.3)
    if timeflow[i].iloc[-1] > 20:
        plt.text(thetime[-1], timeflow[i].iloc[-1], i, fontsize=10)  # 加上文字註解
    count = count + 1
plt.title("爆點分析", fontsize=30)  # 標題
plt.ylabel('主題出現次數', fontsize=20)  # y的標題
plt.xlabel('時間軸', fontsize=20)  # x的標題
plt.tight_layout()
plt.show()
