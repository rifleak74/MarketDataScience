# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:16:10 2019

@author: Ivan
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

############################################################################################################################
#                                                       異動股爬蟲（港股）                                                  #
############################################################################################################################

header = {      
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'et_color=2%3Blight; et_visitor=tmlqmfguf5mqck01d6jhvqeeb5; BIGipServerWebHttpPool=269797386.20480.0000; __auc=07f1bc4416d43040960281945d0; _ga=GA1.3.634144548.1568787401; __gads=ID=46dcbce446919dd5:T=1568787399:S=ALNI_MYd2RfYVGb6u86QK_0nMFU2znxAgQ; PHPSESSID=jm17uef86h2n9o1ts27oj8qs03; et_m_sid=jm17uef86h2n9o1ts27oj8qs03; __asc=f88b0b7c16d492af62c414a9d6f; _gid=GA1.3.1362149993.1568890616; _gat=1',
        'Host': 'www.etnet.com.hk',
        'Referer': 'http://www.etnet.com.hk/www/tc/stocks/sector_hot.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
        }
 # 要抓取的網址
url = 'http://www.etnet.com.hk/www/tc/stocks/blocktrade.php'
#請求網站
list_req = requests.get(url,headers = header)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")

#找到b這個標籤
allRow= soup.findAll('td') 

row=[]
number=[]
name=[]
updown=[]
nominal_price=[]
move=[]
movepercent=[]
high=[]
low=[]
price=[]
currency=[]

for data in range(11,len(allRow)-11,11):
    row.append(allRow[data].text)
    number.append(allRow[data+1].text)
    name.append(allRow[data+2].text)
    if allRow[data+5].text[0] != '-' :
        updown.append('漲')
    else:
        updown.append('跌')
    nominal_price.append(allRow[data+4].text)
    move.append(allRow[data+5].text)
    movepercent.append(allRow[data+6].text)
    high.append(allRow[data+7].text)
    low.append(allRow[data+8].text)
    price.append(allRow[data+9].text)
    currency.append(allRow[data+10].text)
    
result = pd.DataFrame({
        '排序': row,
        '代號': number,
        '名稱': name,
        '漲跌': updown,
        '按盤價': nominal_price,
        '變動': move,
        '變動率': movepercent,
        '最高價': high,
        '最低價': low,
        '成交金額': price,
        '貨幣': currency

        })

