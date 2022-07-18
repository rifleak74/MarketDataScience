# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:47:01 2022

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第六章 Youtube中尋找KOL夥伴
Youtube爬蟲－頻道資料
"""
# selenium
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import pandas as pd
import time
from datetime import datetime

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
time.sleep(5)

# 想爬取的youtube
youtuber = ['c/thisgroupofpeople', # 這群人
            'channel/UCfMiXMUBXxWiVrcXw2GV92g', # 燥咖
            'user/TheN10414', # 又仁
            'channel/UCW_0KHu_E9tH9_WVmrFactg', # 各種同學
            'user/KEVIN0204660', # 反骨男孩
            'user/jasonjason1124', # How Fun
            'user/dionisiojian' # 喬瑟夫
            ]

#準備容器
name = []
pageurl = []
intotime = []
looking = []
subscription = []
description = []
location = []
otherlink = []
channels = []
videolink = []
# 開始一個一個爬蟲
for yChannel in youtuber:

    #--- 簡介 部分
    driver.get('https://www.youtube.com/' + str(yChannel) + '/about')
    time.sleep(10)

    # 基本資料
    name.append(driver.find_element_by_id('text-container').text) # 存youtuber頻道名
    pageurl.append('https://www.youtube.com/' + str(yChannel)) # 存頻道網址

    # 訂閱數輛
    getSubscription = driver.find_element_by_id('subscriber-count').text
    getSubscription = getSubscription.replace(' 位訂閱者','')
    subscription.append(getSubscription)

    # 開始經營時間
    gettime = driver.find_element_by_xpath('//div[@id="right-column"]/yt-formatted-string[2]/span[2]').text
    intotime.append(datetime.strptime(gettime, "%Y年%m月%d日"))

    # 總觀看次數
    getlooking = driver.find_element_by_xpath('//div[@id="right-column"]/yt-formatted-string[3]').text
    getlooking = getlooking.replace('getlooking = ','')
    getlooking = getlooking.replace('觀看次數：','')
    getlooking = getlooking.replace('次','')
    getlooking = getlooking.replace(',','')
    looking.append(int(getlooking))

    description.append(driver.find_element_by_id('description').text) # 存文案

    location.append(driver.find_element_by_xpath('//div[@id="details-container"]/table/tbody/tr[2]/td[2]').text) # 存國家位置

    # 其他連結
    getOtherlink = driver.find_elements_by_xpath('//div[@id="link-list-container"]/a')
    containar = {} # 結果整理成dict
    for link in getOtherlink:
        containar[link.text] = link.get_attribute('href')
    otherlink.append(containar)

    #--- 頻道 部分
    driver.get('https://www.youtube.com/' + str(yChannel) + '/channels')
    time.sleep(10)

    getlink = driver.find_elements_by_id('channel-info')
    containar = {} # 結果整理成dict
    for link in getlink:
        data = link.text
        data = data.split('\n')
        # 檢查有沒有訂閱者
        if len(data) == 1:
            containar[data[0]] = {
                '訂閱數量':0,
                '連結':link.get_attribute('href')
                }
        else:
            containar[data[0]] = {
                '訂閱數量':data[1].replace(' 位訂閱者',''),
                '連結':link.get_attribute('href')
                }
    channels.append(containar)

    #--- 影片 部分
    driver.get('https://www.youtube.com/' + str(yChannel) + '/videos')
    time.sleep(10)

    # 滾動頁面
    for scroll in range(20):
        driver.execute_script('window.scrollBy(0,1000)')
        time.sleep(2)

    containar = [] # 結果整理成list
    for link in driver.find_elements_by_id('video-title'):
        containar.append(link.get_attribute('href'))
    videolink.append(containar)

dic = {
       'Youtuber頻道名稱' : name,
        '頻道網址' : pageurl,
        '開始經營時間' : intotime,
        '總觀看數' : looking,
        '總訂閱數' : subscription,
        '文案' : description,
        '國家位置' : location,
        '其他連結' : otherlink,
        '頻道' : channels,
        '所有影片連結' : videolink
       }
pd.DataFrame(dic).to_csv('Youtuber_頻道資料.csv',
                         encoding = 'utf-8-sig',
                         index=False)
