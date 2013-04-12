# for sina
#coding: utf-8
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
from getWebpage import getWebpage # get the local fname of a webpage
from sysPath import folderPath
from getDetails import getDetails
from extractLinks import extractLinks
from getWebpage import getWebpage
from getSoup import getSoup
import time,datetime,urllib2,urllib
from getSoup import getSoup
from dateutil import parser

def fetchNovel(link):
    content=getWebpage(link)
    soup=BeautifulSoup(content)
    list_c=soup.find('div',{'class':"book_neirong_left"})
    chapters=list_c.findAll('a')
    paras=soup.findAll('div',{'class':'paragraph'})
    intro=soup.find('div',{'class':'bookintro'})
    book_name=''.join(soup.find('title').findAll(text=True)).strip()
    print 'collecting: ',book_name
    for c in chapters:
        url=c['href'][:-4]
        url=url.split('/')
        if len(url)!=5: continue
        page_info = urllib2.build_opener()
        postData='c='+url[-1]+'&b='+url[-2]
        req = urllib2.Request('http://v.book.ifeng.com/book/remc.htm', postData)
        page=page_info.open(req)
        content=page.read()[14:-1]
        content=BeautifulSoup(content)
        f=open(book_name+'.txt','a')
        if content==None: continue
        for y in content.findAll(text=True):
            if y.encode('GBK','ignore').strip()=='': continue
            f.write(y.encode('GBK','ignore')+'\n')
        f.close()

fetchNovel('http://v.book.ifeng.com/book/ts/35777.htm')
