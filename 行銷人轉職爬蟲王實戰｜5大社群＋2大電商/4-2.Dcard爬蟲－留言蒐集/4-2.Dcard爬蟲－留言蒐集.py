# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:18:53 2021
@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com
第四章 Dcard爆點分析
Dcard爬蟲－留言蒐集

更新紀錄
2022/4/23：由於多位學生發現請求API過於頻繁，導致請求出現429，因此加入亂數並拉長請求時間
"""
import time
import requests
import json
import pandas as pd
import random

dcard_article = pd.read_csv('Dcard文章資料.csv')
# https://www.dcard.tw/service/api/v2/posts/235996273/comments?after=60
alldata = []
for articleID in dcard_article['文章ID']:
    last_comment = ''
    url = 'https://www.dcard.tw/service/api/v2/posts/'+ str(articleID) +'/comments'
    doit = True
    i=0
    while doit:
        if i != 0: # 判斷是否是第一次執行
            request_url = url +'?after='+ str(last_comment)
        else:
            request_url = url # 第一次執行，不須加上後方的before
        list_req = requests.get(request_url) # 請求
        #將整個網站的程式碼爬下來
        getdata = json.loads(list_req.content)
        if len(getdata) > 0:
            alldata.extend(getdata) # 將另一個陣列插在最後面
        else:
            doit = False
        
        last_comment = str(len(alldata)) # 取出最後一篇文章
        print(i)
        time.sleep(random.randint(5,15))
        i=i+1

alldata = pd.DataFrame(alldata)
# 翻譯欄位
alldata.rename(columns={
    'id': '發文ID',
    'anonymous': '',
    'postId': '文章ID',
    'createdAt': '發文時間',
    'updatedAt': '更新時間',
    'floor': '樓層',
    'content': '留言內容',
    'likeCount': '按讚數',
    'hiddenByAuthor': '是否被作者隱藏',
    'gender': '性別',
    'school': '學校',
    'host': '是否為發文者',
    'hidden': '是否隱藏',
    'department': '個人主頁',
    }, inplace=True)
#存檔
alldata.to_csv(
    'Dcard留言資料.csv', # 檔案名稱
    encoding = 'utf-8-sig', # 編碼
    index=False # 是否保留index
    ) 
