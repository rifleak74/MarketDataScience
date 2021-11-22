# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:23:27 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第三章 PTT的消費者在意什麼？
PTT爬蟲
"""
import pandas as pd
from Ivan_ptt import crawl_ptt_page

# 使用範例
gossip = crawl_ptt_page(Board_Name ='Gossiping' ,page_num= 1)

# 爬蟲實戰情況
broad = ['folklore','womentalk','boy-girl','Urban_Plan','Gossiping','Nantou','TaichungBun']
containar = pd.DataFrame() # 先準備一個空的容器
for i in broad:
    Elephants = crawl_ptt_page(Board_Name =i ,page_num= 50)
    containar =pd.concat([containar,Elephants],axis=0) # 把新的結果存進容器

#存檔
containar.to_csv(
    'ptt資料.csv', # 檔案名稱
    encoding = 'utf-8-sig', # 編碼
    index=False # 是否保留index
    ) 
