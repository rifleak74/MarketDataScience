# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:18:31 2020

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第十章 贈品：Gmail自動寄信工具
Python寄信基礎－文字樣式教學
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

sendFrom = "寄件者信箱"
senderPassword = "寄件者密碼"
content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "輸入您想要的郵件標題"  #郵件標題
content["from"] = sendFrom  #寄件者
content["to"] = "收件者信箱" #收件者

content.attach(
                MIMEText("""
                        親愛的 <u>Ivan</u>您好：<br><br>
                        
                        想要學Python卻不知從何開始嗎？<b>您有個系統性的選擇！</b> <br>
                        趕快手刀點擊<a href="https://marketingliveincode.com">行銷搬進大程式</a>。
                        
                        """
                        , "html"))  #郵件內容


with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login( sendFrom, senderPassword)  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("成功傳送")
    except Exception as e:
        print("Error message: ", e)
