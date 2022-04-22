# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:09:15 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
Html爬蟲教學Get教學－Yahoo

更新紀錄
2022/4/22：Yahoo舊版網頁全面捨棄，因此修正找不到的標籤
"""
import requests
from bs4 import BeautifulSoup

stock='2002'
 # 要抓取的網址
url = 'https://tw.stock.yahoo.com/q/q?s=' + stock 
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")
#找到th這個標籤
getstock= soup.find('li').text #只抓到第一個<li>
print(getstock)
getstock= soup.findAll('li') #抓到很多個li
#找到b這個標籤
getstock= soup.find('a').text #抓到<b>
print(getstock)
#找到table這個標籤
soup.find('li') #只找到一個
soup.find_all('li') #找到網頁內所有的li
soup.find_all('li', {'id':'root_3'}) #特別指定'id':'root_3'
