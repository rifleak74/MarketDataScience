# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:37:59 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第四章 Dcard爆點分析
Dcard爬蟲－文章資料
"""
import time
import requests
import json
import pandas as pd
# https://www.dcard.tw/service/api/v2/forums/talk/posts?popular=true&limit=30&before=235999153
alldata = []
last_article = ''
url = 'https://www.dcard.tw/service/api/v2/forums/talk/posts?limit=30'
for i in range(5):
    if i != 0: # 判斷是否是第一次執行
        request_url = url +'&before='+ str(last_article)
    else:
        request_url = url # 第一次執行，不須加上後方的before
    list_req = requests.get(request_url) # 請求
    #將整個網站的程式碼爬下來
    getdata = json.loads(list_req.content)
    alldata.extend(getdata) # 將另一個陣列插在最後面
    
    last_article = getdata[-1]['id'] # 取出最後一篇文章
    print(last_article)
    time.sleep(10)
    
alldata = pd.DataFrame(alldata)
# 翻譯欄位
alldata.rename(columns={
    'id': '文章ID',
    'title': '標題',
    'excerpt': '內文簡介',
    'anonymousSchool': '學校匿名',
    'anonymousDepartment': '個人主頁顯示',
    'forumId': '版ID',
    'replyId': '回應的文章ID',
    'createdAt': '發文時間',
    'updatedAt': '更新時間',
    'commentCount': '回覆數',
    'likeCount': '按讚數',
    'topics': '主題標籤',
    'forumName': '版中文名',
    'forumAlias': '版英文名',
    'gender': '作者性別',
    'school': '作者學校',
    'replyTitle': '回應的文章的標題',
    'layout': '頁面版型',
    'withImages': '是否使用圖片',
    'withVideos': '是否使用影片',
    'media': '媒體連結',
    'department': '個人主頁',
    'categories': '類別',
    'link': '連結（版型為連結才有）'
    }, inplace=True)
#存檔
alldata.to_csv(
    'Dcard文章資料.csv', # 檔案名稱
    encoding = 'utf-8-sig', # 編碼
    index=False # 是否保留index
    ) 