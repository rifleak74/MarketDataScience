import requests
from bs4 import BeautifulSoup
###############################################################################
#                         股票行動機器人  【Post爬蟲】                        #
###############################################################################

# 要抓取的網址
url = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2409'
# 附帶的資料必須要有
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36' }

#請求網站
list_req = requests.post(url, headers = headers)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")