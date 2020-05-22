#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:15:08 2020

@author: ivan
"""
# selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import time
import re
import random

useEmail='您的FB帳號'
usePass='您的FB密碼'
catch ='廣告|行銷'
postURL = 'https://www.facebook.com/permalink.php?story_fbid=134084921578475&id=101285581525076'


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
    

####### 開始操作 輸入帳號密碼登入 到fb首頁 ####### 
driver.get("http://www.facebook.com")
time.sleep(1)
assert "Facebook" in driver.title
try:
    elem = driver.find_element_by_id("email")
    elem.send_keys(useEmail)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(usePass)
    elem.send_keys(Keys.RETURN)
except:
    driver.find_element_by_xpath('//*[@name="email"]')
    elem.send_keys(useEmail)
    elem = driver.find_element_by_xpath('//*[@name="pass"]')
    elem.send_keys(usePass)
    elem.send_keys(Keys.RETURN)
time.sleep(5)

#取得帳號絕對ID
try:#舊版
    getID = driver.find_element_by_xpath('//*[@title="個人檔案"]').get_attribute('href')  
    version='old'
except:#新版
    getID = driver.find_element_by_xpath('//div[@data-pagelet="LeftRail"]/div/ul/li/div/a').get_attribute('href')
    version='new'
yourID = getID[getID.find('id=')+3:]

####### 先取得所有的社團 #######
# 切換到自己的社團
driver.get('https://www.facebook.com/profile.php?id=' + yourID + '&sk=groups')

# 滾動頁面
for i in range(30):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    
# 取得所有社團
if len(driver.find_elements_by_xpath('//*[@data-hovercard]')) == 0:
    #新版
    getallgroup = driver.find_elements_by_xpath('//a/span[@dir="auto"]')
else:
    #舊版
    getallgroup = driver.find_elements_by_xpath('//*[@data-hovercard]')
    
get_groups = [] 
#檢查，若無要求就社團全部發
if len(catch) == 0:
    for groups in getallgroup:
        get_groups.append(groups.text)
else:
    for groups in getallgroup:
        if len("".join(re.findall(catch, groups.text))) >0:
            get_groups.append(groups.text)
            
   
'''
只能發送文字形文章，範例如下：
https://www.facebook.com/permalink.php?story_fbid=134084921578475&id=101285581525076
'''
####### 開始分享 #######  
# 切換到文章
driver.get(postURL)
if version == 'new':
    #新版
    for send in get_groups:
        # 按下分享
        driver.find_element_by_xpath('//*[@aria-label="寄送這個給朋友或張貼在你的動態時報中。"]').click()
        time.sleep(random.randint(3,5))
        # 按下分享到社團
        driver.find_element_by_xpath("//*[contains(text(), '分享到社團')]").click()
        time.sleep(random.randint(2,7))
        for send in get_groups:
            # 輸入社團名稱
            driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').send_keys(send)
            time.sleep(random.randint(2,7))
            driver.find_elements_by_xpath('//div[@aria-labelledby]')[-1].click()
            
            length = len(driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').get_attribute('value')) #抓到欲刪除的欄位數量
            driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').send_keys(length * Keys.BACKSPACE) #案幾次刪除
            time.sleep(random.randint(60,120))
else:
    #舊版
    for send in get_groups:
        # 按下分享
        driver.find_element_by_xpath('//*[@title="寄送這個給朋友或張貼在你的動態時報中。"]').click()
        time.sleep(random.randint(3,5))
        # 按下分享到社團
        driver.find_element_by_xpath("//*[contains(text(), '分享到社團')]").click()
        time.sleep(random.randint(2,7))
        # 輸入社團名稱
        driver.find_element_by_xpath('//input[@placeholder="社團名稱"]').send_keys(send)
        time.sleep(random.randint(2,7))
        # 按下向下建選擇第一個最相似的社團
        driver.find_element_by_xpath('//input[@placeholder="社團名稱"]').send_keys('\ue015')
        # 按下enter迴車建
        driver.find_element_by_xpath('//input[@placeholder="社團名稱"]').send_keys('\ue007')
        # 包含原始貼文打勾
        driver.find_element_by_class_name('_55sg').click()
        time.sleep(random.randint(7,15))
        # 發布
        driver.find_elements_by_xpath("//button[contains(text(), '發佈')]")[-1].click()
        time.sleep(random.randint(60,120))
driver.quit()
    
            

