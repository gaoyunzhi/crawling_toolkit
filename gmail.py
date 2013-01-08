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
#receivers=[] #remove this
f.close()
happyNewYear(id='××', pd='××',lst=receivers,
             sub=u'诚邀同游',
             content=u'在下初拟定或在五月末，或在九月初，经由海南，至广东，福建，江浙，终于山东山西，历时一个到一个半月。诚邀同游，即可一路相伴，也可挑选几个景点共赏。具体是几月份出发，会在我intern的事情定下来以后决定，可能需要稍等一个月。有意请回复。'
             +'<br><br>'+u'××')