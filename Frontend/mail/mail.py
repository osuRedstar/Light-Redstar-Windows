# -*- coding:utf-8 -*-
 
import smtplib
from email.mime.text import MIMEText
 
smtp = smtplib.SMTP_SSL('smtp.daum.net', 465)
smtp.ehlo()      # say Hello
smtp.login('support@redstar.moe', 'skchqhdpdy0113')
 
msg = MIMEText('본문 테스트 메시지')
msg['Subject'] = '테스트'
msg['To'] = 'jeonkangheun@gmail.com'
smtp.sendmail('support@redstar.moe', 'jeonkangheun@gmail.com', msg.as_string())
 
smtp.quit()