# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:33:25 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
Html爬蟲實戰－FoodPanda爬蟲
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
#2021/7/25 新增
head = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'addressConfigProviderTracked=true; dhhPerseusGuestId=1625726240.4408702442.GmccdWqdtL; ld_key=140.118.208.41; hl=en; dhhPerseusSessionId=1627183075.3261760923.4NyCItW2TA; AppVersion=c56ae2e; __cf_bm=b4ce7934e8c55f7628beb51ec8156da550d6e84a-1627183075-1800-Aau8DKX/eO1lewsBQ07uG2BnnUU/yqlOWXal75M8/cBQJO+WGD1JMV1ISno1mqnYySDl0KSkdTV+IY/chjtpCHI=; _pxhd=dEvSpWwn2ATDv8WZ7QqHtWMxKv/MksYSRbAZUt8vbVK6SpHOrN0qzhDntF4oyGsrAYt6p5aKVpjhqvrzmkr6FQ==:qtU5hZQwOoKM5J0AUwVLPnM0Z8yGHQgBSEa1nL6dTrLWaf3HXMTd2ItYO-hy2k1CjZLH2xa9Ivt5jprnHBUWXAnmLXme4UVFxxCJ-EwY88E=; dhhPerseusHitId=1627183077926.349296501302744260.osgev2xwtl',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }

# 要抓取的網址
url = 'https://www.foodpanda.com.tw/en/city/taipei-city'
#請求網站
list_req = requests.get(url,headers = head)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")
getall = soup.findAll('figcaption',{'class':'vendor-info'}) #取得所有店家
i = getall[0] # 先看第一個商店

print(i.find('span',{'class':'name'}).text) #取得店家名稱
print(i.find('strong').text) #取得評分
print(i.find('li',{'class':'vendor-characteristic'}).text) #取得標籤
#取得外送費用
print(i.find('li',{'class':'delivery-fee'}).text) # 2021/7/25修改
part1 = i.find('li',{'class':'delivery-fee'}) # 2021/7/25修改
part2 = part1.find({'strong'})
part2.text

# 整理成資料表
shopName = []
star = []
tag = []
shipping = []
for i in getall:
    shopName.append(i.find('span',{'class':'name'}).text)
    star.append(i.find('strong').text)
    tag.append(i.find('li',{'class':'vendor-characteristic'}).text)
    
    part1 = i.find('li',{'class':'delivery-fee'}) # 2021/7/25修改
    part2 = part1.find({'strong'})
    part2.text
    shipping.append(part2.text)
    
pd.DataFrame({
    '店家名稱':shopName,
    '評分':star,
    '標籤':tag,
    '外送費用':shipping
    }).to_csv('foodpanda.csv', encoding='utf-8-sig', index=False)