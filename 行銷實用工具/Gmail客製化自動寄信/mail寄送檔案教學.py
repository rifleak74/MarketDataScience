# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:18:31 2020

@author: Ivan
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from email.mime.application import MIMEApplication 

content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "測試寄信"  #郵件標題
content["from"] = "ivanyang0606@gmail.com"  #寄件者
content["to"] = "aaaaaa111111aaaaaa1111ox@gmail.com" #收件者
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
pdfload.add_header('Content-Disposition', 
                   'attachment', 
                   filename=fileName) 
content.attach(pdfload) 

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("ivanyang0606@gmail.com", "cvztwtflzkntbuql")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("成功傳送")
    except Exception as e:
        print("Error message: ", e)