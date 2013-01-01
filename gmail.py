#coding: utf-8
#don't push to public with your gmail password!!!!!!!

import smtplib
import os

def happyNewYear(id,pd,lst,sub,content):
   

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    #mailServer.ehlo()
    mailServer.login(id, pd)
    for rec in lst:
        try:
            headers = ["from: " + id,
               "subject: " + sub,
               "to: " + rec,
               "mime-version: 1.0",
               "content-type: text/html"]
            headers = "\r\n".join(headers)
            msg=headers + "\r\n\r\n" +content
            mailServer.sendmail(id, rec, msg)
        except:
            print rec+'\tfailed'
    mailServer.close()
    
f=open('emails.txt')
receivers=[]
for line in f:
    addr=line.strip()
    if '@' in addr: receivers.append(addr)
#receivers=[] #remove this
f.close()
happyNewYear(id='**', pd='**',lst=receivers,
             sub=u'新年快乐',content=u'新年快乐！祝新的一年里身体健康，万事如意！'+'<br><br>'+u'**')