# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:51:00 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第三章 PTT的消費者在意什麼？
消費者關鍵字分析
"""
import jieba
import jieba.analyse
import pandas as pd
getdata = pd.read_csv('ptt資料.csv', encoding = 'utf-8-sig')
getdata.columns

# 挑出 標題 or 內文 or 所有留言 中，有出現「花襯衫」這個字詞的文章
get_shirt_data = getdata[
    getdata['標題'].str.contains('花襯衫') |
    getdata['內文'].str.contains('花襯衫') |
    getdata['所有留言'].str.contains('花襯衫')
    ]

#--- 先行填滿空值
get_shirt_data['標題'] = get_shirt_data['標題'].fillna('')
get_shirt_data['內文'] = get_shirt_data['內文'].fillna('')
get_shirt_data['所有留言'] = get_shirt_data['所有留言'].fillna('')
allstr = get_shirt_data['標題'].sum() + get_shirt_data['內文'].sum() + get_shirt_data['所有留言'].sum() # 將標題與內文全部串起來

#--- 取代掉無意義字元
replaceList = ['span','https','com','imgur','class','jpg','f6','href','rel',
               'nofollow','..','target','blank','hl','www','cc','tw','XD','f3',
               'f2','reurl','Re','http','amp','content','type','user','ipdatetime',
               '[',']','{','}','(',')',"'",':',',','/','\n','，','"','→','.','=','>',
               '>','<','？','。','_','！','、','?','：','-','（','~','～','）','「',
               '!','」','…','^',';','─','QQ','&','—',':',',','/','★','｜','+']
for i in replaceList:
    allstr = allstr.replace(i,'')

# 用TF-IDF演算法，尋找top 100 關鍵字
keywords_top=jieba.analyse.extract_tags(allstr, # 字詞
                                        topK=100, # 前幾名
                                        withWeight=True) # 是否要計算分數

# 土法煉鋼計算字詞
words = jieba.cut(allstr)
df_words = pd.DataFrame(list(words))
df_value_counts = df_words.value_counts()

for i in range(100):
    print(df_value_counts.index[i])
    
# 觀看原始資料
import re
findword = 'UQ'
for m in re.finditer(findword, allstr): #進行資料比對
    print(
        allstr[m.start()-50 : m.start()] + # 關鍵字的前50個字
        '【'+findword+'】' + # 關鍵字本身
        allstr[m.start()+len(findword): m.start()+50]+'\n' # 關鍵字的後50個字
        ) 
    