# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:23:37 2021
@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com
第二章 進階皇蟲Selenium
Selenium實戰練習－UberEat爬蟲
"""
# selenium，2022/9/17 將套件更新到4.4.3版本，因此寫法全部都更新過
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# 自動下載ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# 開啟瀏覽器
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
time.sleep(5)

# 開啟網頁
driver.get('https://www.ubereats.com/tw')
time.sleep(3)



#---------- 開始網頁的控制 ----------
#--- 輸入外送地址
getblock = driver.find_element(by=By.XPATH, value='//*[@placeholder="輸入外送地址"]')
getblock.send_keys('中山北路二段1號') # 輸入地址
time.sleep(1)
getblock.send_keys('\ue007') # 按下Enter

#--- 目標：爬下所有餐廳門市
#方法1：利用class抓取
#由於網站更新後，class都是程式自動不好抓取，改抓取個餐點種類的大類別
len(driver.find_elements(by=By.TAG_NAME, value='section'))

# show出各個類別
for i in driver.find_elements(by=By.TAG_NAME, value='section'):
    # show 出所有店名
    for j in i.find_elements(by=By.TAG_NAME, value='h3'):
        print(j.text + '\n')


len(driver.find_elements(by=By.XPATH, value='//section/div[2]/div[1]/li'))
# selenium，2022/11/06 ubereat網頁有更新，因此有些調整
#方法2：利用剝洋蔥方式
location = '//section/div[2]/div[1]/li'
getAllShop = driver.find_elements(by=By.XPATH, value=location) # 先抓到大類別
for i in range(0, 4): # 只先 show 出3個店家名稱看看
    print(getAllShop[i].find_element(by=By.TAG_NAME, value='h3').text)

# 整頁的店家名稱都吐出來
for i in getAllShop:
    try:
        print(i.find_element(by=By.TAG_NAME, value='h3').text)
    except:
        print('這不是店家') # 可能會抓到網頁的廣告，因此需要跳過




# 完整寫法
restaurant = []
restaurantURL = []
deliveryCost = []
spendTime = []
location = '//section/div[2]/div[1]/li'
getAllShop = driver.find_elements(by=By.XPATH, value=location) # 先抓到大類別
for i in getAllShop:
    # 先嘗試取得該標籤的陣列
    get_restaurant = i.find_elements(by=By.TAG_NAME, value='h3')
    get_restaurantURL = i.find_elements(by=By.TAG_NAME, value='a')
    get_deliveryCost = i.find_elements(by=By.XPATH, value='div/div/div/div[2]/div[2]/div[2]')
    get_spendTime = i.find_elements(by=By.XPATH, value='div/div/div/div[2]/div[2]/div[3]')

    # 檢查是否有抓到資料，有可能有些沒抓到，譬如有店家沒有顯示外送價格，這會導致等等打包csv檔案時出錯
    if len(get_restaurant)>0 and len(get_restaurantURL)>0 and len(get_deliveryCost)>0 and len(get_spendTime)>0 :
        restaurant.append(get_restaurant[0].text)
        restaurantURL.append(get_restaurantURL[0].get_attribute('href'))
        deliveryCost.append(get_deliveryCost[0].text)
        spendTime.append(get_spendTime[0].text)
    else:
        print('這不是店家，或資料有缺少') # 可能會抓到網頁的廣告，或者沒有運送價格、時間等等
    

# 打包成CSV檔案
dfData = pd.DataFrame({
    '店家名稱':restaurant,
    '網址':restaurantURL,
    '運費':deliveryCost,
    '運送時間':spendTime
    })
dfData.to_csv('UberEat.csv', encoding = 'utf-8-sig', index = False)




#--- 補充資源
driver.find_elements(by=By.ID, value='batBeacon872942032971') # 通過ID
# <input type="text" class="form-control" id="usr" name='inportbox1'>
driver.find_elements(by=By.NAME, value='inportbox1') # 通過Name
driver.find_elements(by=By.LINK_TEXT, value='GABA 元気の源 嘎吧 日式飯糰店') # 通過連結
driver.find_elements(by=By.TAG_NAME, value='h1') # 通過標籤
driver.find_elements(by=By.CSS_SELECTOR, value='div.h3') #通過標籤CSS
