import requests
import pandas as pd
from bs4 import BeautifulSoup

 # 要抓取的網址
url = 'http://mops.twse.com.tw/mops/web/ajax_t05st01'

my_headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', 
              'Referer': 'http://mops.twse.com.tw/mops/web/t05st01',# 必要 
              'Cookie': 'jcsession=jHttpSession@5bd6be0c; _ga=GA1.3.32395516.1542113354; _gid=GA1.3.1756921164.1542336195; newmops2=co_id%3D2002%7Cyear%3D107%7Cmonth%3D%7Cb_date%3D%7Ce_date%3D%7C'# 必要 
} 


data  = {
            'encodeURIComponent': '1',
            'step': '1',
            'firstin': '1',
            'off': '1',
            'TYPEK': 'all',
            'co_id': '2002',
            'year': '107'
        }

r_post  =  requests.post(url, data = data, headers  =  my_headers, timeout  =  5).text
soup  =  BeautifulSoup(r_post, 'html.parser')
gettable = soup.find('table', {'class':'hasBorder'})
gettitle = soup.find_all('pre')