# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 09:18:22 2022

@author: ivan
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
    
    geturl = driver.find_elements_by_xpath('//h2/a')

    for j in geturl:
        theurl.append(j.get_attribute('href'))
        
    time.sleep(5)
    
brand = []
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
productDscrp = []
global_range = []
view_url = []
for page in range(140,len(theurl)):
    print('第 '+ str(page) + ' 個商品')
    #儲存網址
    url.append(theurl[page])
    
    # 去到你想要的網頁
    driver.get(theurl[page])
    time.sleep(randint( 7, 15))
    
    # 品牌名稱
    if len(driver.find_elements_by_id('bylineInfo')) == 0 :
        brand.append('沒有牌子')
    else:
        brand.append(driver.find_element_by_id('bylineInfo').text)
    
    # 商品名稱
    title.append(driver.find_element_by_id('title').text) 
    
    #商品定價
    if len(driver.find_elements_by_id('corePriceDisplay_desktop_feature_div'))==0:
        getprice = driver.find_element_by_id('corePrice_desktop').text
    else:
        getprice = driver.find_element_by_id('corePriceDisplay_desktop_feature_div').text
    
    getprice = getprice.replace('US$','') # 先把「US$」拿掉
    if '有了交易' in getprice:
        getprice = getprice[getprice.find('有了交易')+6:]
        getprice = getprice.split('\n')[0]
    else:
        
        getprice = getprice.replace('定價：','') # 把「US$」拿掉
        if ' -' in getprice: # 利用「 - 」來切割兩個數字
            getprice = getprice.replace('\n','') # 把「US$」拿掉
            cutlist = getprice.split(' -')
            getprice = (float(cutlist[0]) + float(cutlist[1]))/2 # 計算平均
        else:
            getprice = getprice.replace('\n','.')
    price.append(getprice)
    
    
    # 星星評分
    if len(driver.find_elements_by_id('acrPopover'))==0:
        star.append('沒有星等')
    else:
        star.append(driver.find_element_by_id('acrPopover').get_attribute("title").replace(' 顆星，最高 5 顆星',''))
    # 全球評分數量
    if len(driver.find_elements_by_id('acrCustomerReviewText'))==0:
        starNum.append(0)
    else:
        getglobalNum = driver.find_element_by_id('acrCustomerReviewText').text
        getglobalNum = getglobalNum.replace('等級','')
        getglobalNum = getglobalNum.replace(',','')
        starNum.append(getglobalNum)
    
    # 客戶回饋大小
    if len(driver.find_elements_by_id('fitRecommendationsLinkRatingText')) == 0:
        toosmall.append(0)
        small.append(0)
        goodsize.append(0)
        big.append(0)
        toobig.append(0)
    else:
        time.sleep(5)
        driver.find_element_by_id('fitRecommendationsLinkRatingText').click()
        time.sleep(5)
        getrequest = driver.find_elements_by_xpath('//td[@class = "a-span1 a-nowrap"]')
        toosmall.append(getrequest[0].text)# 太小
        small.append(getrequest[1].text)# 有點小
        goodsize.append(getrequest[2].text)# 尺寸正確
        big.append(getrequest[3].text)# 有點大
        toobig.append(getrequest[4].text)# 太大
        # 關閉選項
        if len(driver.find_elements_by_xpath('//button[@data-action = "a-popover-close"]')) != 0:
            driver.find_element_by_xpath('//button[@data-action = "a-popover-close"]').click()
        time.sleep(5)
    
    # 大小選項
    driver.find_element_by_xpath('//span[@data-csa-interaction-events = "click"]').click()
    time.sleep(5)
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
    if len(driver.find_elements_by_id('productDescription')) != 0:
        productDscrp.append(driver.find_element_by_id('productDescription').text)
    else:
        productDscrp.append('')
    
    # 產品詳細資訊
    description.append(driver.find_element_by_id('detailBullets_feature_div').text)
    # 全球排名
    getdata = driver.find_element_by_xpath('//div[@id = "detailBulletsWrapper_feature_div"]/ul').text
    getdata = getdata.replace('暢銷商品排名: ','')
    # getdata = getdata.replace('\n','')
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
    if len(driver.find_elements_by_xpath('//a[@data-hook = "see-all-reviews-link-foot"]'))== 0 :
        view_url.append('沒有留言')
    else:
        view_url.append(driver.find_element_by_xpath('//a[@data-hook = "see-all-reviews-link-foot"]').get_attribute('href'))
    
    dic = {
           '品牌名稱' : brand,
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
            '產品資訊' : productDscrp,
            '全球排名' : global_range,
            '留言網址' : view_url
           }
    if page%10==9:
        pd.DataFrame(dic).to_csv(
                '到第'+str(page)+'頁_Amazon商品資料.csv', # 檔案名稱
                encoding = 'utf-8-sig', # 編碼
                index=False # 是否保留index
                )
pd.DataFrame(dic).to_csv(
        'Amazon商品資料.csv', # 檔案名稱
        encoding = 'utf-8-sig', # 編碼
        index=False # 是否保留index
        )
