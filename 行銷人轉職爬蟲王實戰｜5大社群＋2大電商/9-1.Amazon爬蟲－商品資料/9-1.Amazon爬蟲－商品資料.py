# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:16:20 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第九章 Amazon告訴您市場缺口
Amazon爬蟲－商品資料
"""
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import time
from random import randint
import pandas as pd
thing = '花襯衫'

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

theurl = []
for i in range(5):
    # 去到你想要的網頁
    driver.get("https://www.amazon.com/s?k="+ thing +"&page="+ str(i) +"ref=sr_pg_2")
    
    geturl = driver.find_elements_by_xpath('//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a[@class="a-link-normal a-text-normal"]')

    for j in geturl:
        theurl.append(j.get_attribute('href'))
        
    time.sleep(5)
    
title = []
url = []
price = []
star = []
starNum = []
toosmall = []
small = []
goodsize = []
big = []
toobig = []
size_options = []
color_options = []
description = []
global_range = []
view_url = []
for page in theurl:
    #儲存網址
    url.append(page)
    
    # 去到你想要的網頁
    driver.get(page)
    time.sleep(randint( 7, 15))
    # if "休閒扣領襯衫" in driver.find_element_by_id('wayfinding-breadcrumbs_feature_div').text:
        
    # 商品名稱
    title.append(driver.find_element_by_id('title').text) 
    
    #商品定價
    if len(driver.find_elements_by_id('priceblock_ourprice')) == 0:
        price.append(None)
    else:
        getprice = driver.find_element_by_id('priceblock_ourprice').text
        getprice = getprice.replace('US$','') # 先把「US$」拿掉
        if ' - ' in getprice: # 利用「 - 」來切割兩個數字
            cutlist = getprice.split(' - ')
            getprice = (float(cutlist[0]) + float(cutlist[1]))/2 # 計算平均
        price.append(getprice)
    
    # 星星評分
    star.append(driver.find_element_by_id('acrPopover').get_attribute("title"))
    # 全球評分數量
    getglobalNum = driver.find_element_by_id('acrCustomerReviewText').text
    starNum.append(getglobalNum)
    # 太小
    toosmall.append(driver.find_elements_by_xpath('//td[@class = "a-span1 a-nowrap"]')[0].text)
    # 有點小
    small.append(driver.find_elements_by_xpath('//td[@class = "a-span1 a-nowrap"]')[1].text)
    # 尺寸正確
    goodsize.append(driver.find_elements_by_xpath('//td[@class = "a-span1 a-nowrap"]')[2].text)
    # 有點大
    big.append(driver.find_elements_by_xpath('//td[@class = "a-span1 a-nowrap"]')[3].text)
    # 太大
    toobig.append(driver.find_elements_by_xpath('//td[@class = "a-span1 a-nowrap"]')[4].text)
    
    # 大小選項
    containar = []
    for i in driver.find_elements_by_xpath('//li[contains(@id, "size_name_")]'):
        if i.text != '選擇' and i.text != '':
            containar.append(i.text)
    size_options.append(containar)
    
    # 顏色選項
    containar = []
    for i in driver.find_elements_by_xpath('//li[contains(@id, "color_name_")]'):
        getdata = i.get_attribute("title")
        containar.append(getdata.replace('請按下選擇 ','')) # 取代掉「請按下選擇」
    color_options.append(containar)

    # 商品描述
    description.append(driver.find_element_by_id('productDescription').text)
    # 全球排名
    getdata = driver.find_element_by_id('SalesRank').text
    getdata = getdata.replace('\n','')
    getdata = getdata.split('#')
    containar = {}
    for i in range(1,len(getdata)):
        rang = getdata[i].split(' 在 ')[0]
        item = getdata[i].split(' 在 ')[1]
        if ' (' in item:
            item = item.split(' (')[0]
        containar[item] = int(rang.replace(',',''))
    global_range.append(containar)
    
    # 留言網址
    view_url.append(driver.find_element_by_xpath('//a[@data-hook = "see-all-reviews-link-foot"]').get_attribute('href'))

dic = {
       '商品名稱' : title,
        '網址' : url,
        '商品定價' : price,
        '星星評分' : star,
        '全球評分數量' : starNum,
        '太小' : toosmall,
        '有點小' : small,
        '尺寸正確' : goodsize,
        '有點大' : big,
        '太大' : toobig,
        '大小選項' : size_options,
        '顏色選項' : color_options,
        '商品描述' : description,
        '全球排名' : global_range,
        '留言網址' : view_url
       }
pd.DataFrame(dic).to_csv(
        'Amazon商品資料.csv', # 檔案名稱
        encoding = 'utf-8-sig', # 編碼
        index=False # 是否保留index
        )