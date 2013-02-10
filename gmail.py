#coding: utf-8
#don't push to public with your gmail password!!!!!!!

import smtplib
import os
from email.header import Header

def happyNewYear(id,pd,lst,sub,content):
   

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    #mailServer.ehlo()
    mailServer.login(id, pd)
    for rec in lst:
        try:
            headers = ["from: " + id,
               "subject: " + str(Header(sub, 'utf-8')),
               "to: " + rec,
               "mime-version: 1.0",
               "content-type: text/html"]
            headers = "\r\n".join(headers)
            msg=headers + "\r\n\r\n" +content
            mailServer.sendmail(id, rec, msg)
        except:
            print rec,'failed'

    mailServer.close()
    
f=open('emails.txt')
receivers=[]
for line in f:
    addr=line.strip()
    if '@' in addr: receivers.append(addr)
receivers=['gyz@mit.edu'] #remove this
f.close()
happyNewYear(id='', pd='',lst=receivers,
             sub=u'',
             content=u'能不能帮忙like一下我们team做的网页？请至 http://6.470.scripts.mit.edu/webbys/ 拉到最后，喜欢"Apparate"就可以了！谢谢!我和两个很可爱的双胞胎一起写的程序！<br><br>高韫之')