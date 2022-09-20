# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:56:29 2021
@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com
第五章 IG增粉大師
IG登入
"""
# selenium，2022/9/17 將套件更新到4.4.3版本，因此寫法全部都更新過
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

IGID = '您的IG帳號'
IGpassword = '您的IG密碼'

# 自動下載ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
# 以下三個註解打開，瀏覽器就不會開啟
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("prefs",prefs)

# 開啟瀏覽器
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
time.sleep(5)

####### 開始操作 輸入帳號密碼登入 到IG首頁 ####### 
driver.get("https://www.instagram.com/")
time.sleep(1)
assert "Instagram" in driver.title

time.sleep(3)
driver.find_element(By.XPATH, value='//*[@name="username"]').send_keys(IGID) #輸入登入帳號
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@name="password"]').send_keys(IGpassword) # 輸入登入密碼
time.sleep(3)

driver.find_element(By.XPATH, value='//*[@type="submit"]').click()
time.sleep(3)
driver.find_elements(By.XPATH, value='//*[@type="button"]')[1].click() #是否儲存瀏覽器資料，「稍後再說」
