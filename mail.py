#!/usr/bin/python 
#-*- coding:utf-8 -*-
"""
Source: https://shumeipai.nxez.com/2020/01/02/send-email-raspberry-pi-ip-with-python.html
"""
import smtplib 
from email.mime.text import MIMEText 
import sys  
mail_host = 'smtp.163.com'   #smtp地址如果不知可以百度如“163邮箱smtp地址”
mail_user = 'user@163.com'           #此账号密码是用来给人发送邮件的
mail_pass = 'password'           #此账号密码是用来给人发送邮件的
mail_postfix = '163.com'   #邮箱地址，smtp地址删去smtp字符如“163.com”
  
def send_mail(to_list,subject,content): 
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content) 
    msg['Subject'] = subject 
    msg['From'] = me 
    msg['to'] = to_list 
      
    try: 
        s = smtplib.SMTP_SSL() 
        s.connect(mail_host) 
        s.login(mail_user,mail_pass) 
        s.sendmail(me,to_list,msg.as_string()) 
        s.close() 
        return True
    except Exception,e: 
        print str(e) 
        return False
      
if __name__ == "__main__": 
        send_mail(sys.argv[1], sys.argv[2], sys.argv[3]) 
