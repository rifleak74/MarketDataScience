# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:56:29 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第五章 IG增粉大師
IG登入
"""
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import time

IGID = '您的IG帳號'
IGpassword = '您的IG密碼'

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

driver.find_element_by_xpath('//*[@type="submit"]').click()
time.sleep(3)
driver.find_elements_by_xpath('//*[@type="button"]')[1].click() #是否儲存瀏覽器資料，「稍後再說」
