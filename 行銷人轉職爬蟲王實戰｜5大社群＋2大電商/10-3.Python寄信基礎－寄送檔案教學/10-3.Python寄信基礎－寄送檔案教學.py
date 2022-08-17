# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:18:31 2020

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第十章 贈品：Gmail自動寄信工具
Python寄信基礎－寄送檔案教學
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from email.mime.application import MIMEApplication 


sendFrom = "寄件者信箱"
senderPassword = "寄件者密碼"
content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "輸入您想要的郵件標題"  #郵件標題
content["from"] = sendFrom  #寄件者
content["to"] = "收件者信箱" #收件者


content.attach(MIMEText("Ivan的測試寄信，寄信處女作品～～"))  #郵件內容
content.attach(MIMEImage(Path("夕陽.jpg").read_bytes()))  # 郵件圖片內容

#寄送PDF檔案
fileName = 'test.pdf'
pdfload = MIMEApplication(open(fileName,'rb').read()) 
pdfload.add_header('Content-Disposition', 
                   'attachment', 
                   filename=fileName) 
content.attach(pdfload) 

#寄送Word檔案
fileName = 'test.docx'
pdfload = MIMEApplication(open(fileName,'rb').read()) 
pdfload.add_header('Content-Disposition', 
                   'attachment', 
                   filename=fileName) 
content.attach(pdfload) 

#寄送csv檔案
fileName = '顧客訂單.csv'
pdfload = MIMEApplication(open(fileName,'rb').read()) 
pdfload.add_header('Content-Disposition', # 內容配置
                   'attachment', # 附件
                   filename=fileName) 
content.attach(pdfload) 

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login( sendFrom, senderPassword)  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("成功傳送")
    except Exception as e:
        print("Error message: ", e)
