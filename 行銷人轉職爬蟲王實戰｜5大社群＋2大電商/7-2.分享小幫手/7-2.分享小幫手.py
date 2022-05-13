# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:06:55 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第七章 FB自動發社團發文小幫手
分享小幫手
"""
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import time
import random

useEmail = '帳號'
usePass = '密碼'
catchk_keyword = ['廣告'] # 想要發文的社團，而該社團名字中出現的字詞
identity = '楊超霆' # 發文身分
content = '#python\n #好物物推薦' # 發文文章內容
postURL = 'https://www.facebook.com/marketingliveincode/posts/1590865937778957' #所分享的文章

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

# 發文準備
def goto_post(keyword):
    driver.get(postURL)# 切換到想發的文章
    time.sleep(10)
    
    # 點選分享社團
    driver.find_element_by_xpath('//div[@aria-label="寄送這個給朋友或張貼在你的動態時報中。"]').click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[contains(text(), '分享到社團')]").click()
    time.sleep(3)
    
    # 切換分享身分
    driver.find_element_by_xpath('//label[@aria-label="使用以下身分分享"]').send_keys('\ue015')
    time.sleep(5)
    get_all_identity = driver.find_elements_by_xpath('//div[@aria-checked="false"]')
    for getid in get_all_identity:
        if getid.text == identity:
            getid.click()
            break;
    time.sleep(5)
    
    # 將Keyword放入，搜尋社團
    driver.find_element_by_xpath('//input[@aria-label="搜尋社團"]').send_keys(keyword)
    time.sleep(3)


#一個個關鍵字進去
for keyword in catchk_keyword:
    goto_post(keyword) # 執行發文準備

    # 計算該關鍵字共有幾個社團
    count = len(driver.find_elements_by_xpath('//div[@style="padding-left: 8px; padding-right: 8px;"]/div[@role="button"]'))
    time.sleep(random.randint(5,10))
    
    temp = 0 # 用來記錄已發文的社團
    for long in range(count):
        if long != 0: # 若不是第一次執行，則需要再次執行發文準備，因為發過文後「分享」按鈕會消失
            goto_post(keyword) 
            
        getdriver = driver.find_elements_by_xpath('//div[@style="padding-left: 8px; padding-right: 8px;"]/div[@role="button"]')[temp]
        if len(getdriver.text) == 0: # 檢查
            print('抓到空物件，下一個')
        else:
            # 點進社團
            getdriver.click()
            
            # 發文
            time.sleep(random.randint(3,5))
            try:
                driver.find_element_by_xpath('//div[@aria-label="留個言吧......"]').send_keys(content)
            except:
                driver.find_element_by_xpath('//div[@aria-label="建立公開貼文……"]').send_keys(content)
            time.sleep(random.randint(3,5))
            driver.find_element_by_xpath('//input[@aria-checked="false"]').click()
            time.sleep(random.randint(2,5))
            driver.find_element_by_xpath('//div[@aria-label="發佈"]').click()
            time.sleep(random.randint(6,12))
        
        temp = temp + 1 # 記錄已發文的社團
        
    time.sleep(random.randint(20,50))


