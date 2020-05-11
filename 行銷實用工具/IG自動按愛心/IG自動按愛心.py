# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:18:55 2019

@author: Ivan
"""
# selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import random
import time

IGID = '你的IG帳號'
IGpassword = '你的IG密碼'
tags=['guitar','guitarcover','music','piano']

# 設定基本參數
desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
#此處必須換成自己電腦的User-Agent
desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

# PhantomJS driver 路徑 似乎只能絕對路徑
driver = webdriver.PhantomJS(executable_path = 'phantomjs', desired_capabilities=desired_capabilities)

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# 以下三個註解打開，瀏覽器就不會開啟
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# 開啟瀏覽器
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

####### 開始操作 輸入帳號密碼登入 到IG首頁 ####### 
driver.get("https://www.instagram.com/")
time.sleep(1)
assert "Instagram" in driver.title

time.sleep(3)
driver.find_element_by_xpath('//*[@name="username"]').send_keys(IGID) #輸入登入帳號
time.sleep(1)
driver.find_element_by_xpath('//*[@name="password"]').send_keys(IGpassword) # 輸入登入密碼
time.sleep(3)



####### 開始操作 到不同的tag去發文 ####### 
for tag in tags:
    driver.get("https://www.instagram.com/explore/tags/" + tag) #切換到該tag
    time.sleep(random.randint(2,5))
    driver.find_elements_by_class_name('_9AhH0')[9].click() #點選圖片(選擇最新發的)
    for i in range(random.randint(40,50)):
        if i % 10 == 1:
            time.sleep(random.randint(5,20))
        
        # 檢查有沒有按過讚
        if len(driver.find_elements_by_xpath('//*[@aria-label="Unlike"]')) != 0 or len(driver.find_elements_by_xpath('//*[@aria-label="收回讚"]')) != 0:
            print('按過了')
        else:
            time.sleep(random.randint(1,3))
            try:
                driver.find_element_by_xpath('//*[@aria-label="讚"]').click()
            except:
                print('圖片沒跑出來，直接下一頁')
        driver.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
        time.sleep(random.randint(1,5))
        
    print(tag +' 按完了')
    time.sleep(random.randint(7,15)) # 按完一個tag稍微休息一下，盡量模仿真人