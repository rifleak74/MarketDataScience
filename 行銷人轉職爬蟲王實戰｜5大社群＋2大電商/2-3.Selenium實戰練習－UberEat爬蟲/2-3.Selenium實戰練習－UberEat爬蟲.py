# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:23:37 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第二章 進階皇蟲Selenium
Selenium實戰練習－UberEat爬蟲
"""
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# 設定基本參數
desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
#此處必須換成自己電腦的User-Agent
desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

# PhantomJS driver 路徑
driver = webdriver.PhantomJS(executable_path = 'phantomjs', desired_capabilities=desired_capabilities)

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# 開啟瀏覽器
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

# 去到你想要的網頁
driver.get("https://www.ubereats.com/tw")
time.sleep(3)



#---------- 開始網頁的控制 ----------
#--- 輸入外送地址
getblock = driver.find_element_by_xpath('//*[@placeholder="輸入外送地址"]')
getblock.send_keys('中山北路二段1號') # 輸入地址
time.sleep(1)
getblock.send_keys('\ue007') # 按下Enter

#--- 目標：爬下所有餐廳門市
#方法1：利用class抓取
len(driver.find_elements_by_class_name('lv'))
len(driver.find_elements_by_class_name('g3'))
len(driver.find_elements_by_class_name('ag'))

for i in driver.find_elements_by_class_name('lv'):
    print(i.text + '\n')

#方法2：利用剝洋蔥方式
location = '//main/div/div[3]/div[2]/div/div[4]/div['
# driver.find_element_by_xpath('//main/div/div[3]/div[2]/div/div[4]/div[1]/div/a/h3')
for i in range(1, 21):
    print(driver.find_element_by_xpath(location + str(i) + ']/div/a/h3').text + ' ')

doit = True
i = 1
while doit:
    try:
        print(driver.find_element_by_xpath(location + str(i) + ']/div/a/h3').text + ' ')
    except:
        doit = False
        print(i)
    i = i + 1

# 完整寫法
restaurant = []
restaurantURL = []
deliveryCost = []
spendTime = []
location = '//main/div/div[3]/div[2]/div/div[4]/div['
doit = True
i = 1
while doit:
    try:
        restaurant.append(driver.find_element_by_xpath(location + str(i) + ']/div/a/h3').text)
        restaurantURL.append(driver.find_element_by_xpath(location + str(i) + ']/div/a').get_attribute('href'))
        deliveryCost.append(driver.find_element_by_xpath(location + str(i) +']/div/div/div/div[2]/div[2]/div[2]').text)
        spendTime.append(driver.find_element_by_xpath(location + str(i) +']/div/div/div/div[2]/div[2]/div[3]').text)
    except:
        doit = False
    print(i)
    i = i + 1
    
# 打包成CSV檔案
dfData = pd.DataFrame({
    '店家名稱':restaurant,
    '網址':restaurantURL,
    '運費':deliveryCost,
    '運送時間':spendTime
    })
dfData.to_csv('UberEat.csv', encoding = 'utf-8-sig', index = False)




#--- 補充資源
driver.find_element_by_id('batBeacon872942032971') # 通過ID
# <input type="text" class="form-control" id="usr" name='inportbox1'>
driver.find_element_by_name('inportbox1') # 通過Name
driver.find_element_by_link_text('GABA 元気の源 嘎吧 日式飯糰店') # 通過連結
driver.find_element_by_tag_name('h1') # 通過標籤
driver.find_element_by_css_selector('div.h3') #通過標籤CSS
