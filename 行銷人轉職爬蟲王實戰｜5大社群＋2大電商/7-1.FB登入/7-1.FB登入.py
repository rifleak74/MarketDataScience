# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:02:59 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第七章 FB自動發社團發文小幫手
FB登入
"""
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import time
    
useEmail = '帳號'
usePass = '密碼'

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

# 開啟瀏覽器
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

driver.get("http://www.facebook.com")
time.sleep(3)
assert "Facebook" in driver.title

driver.find_element_by_id('email').send_keys(useEmail) # 輸入帳號
time.sleep(3)
driver.find_element_by_id('pass').send_keys(usePass) # 輸入密碼
time.sleep(1)
driver.find_element_by_name('login').click() # 按下登入
