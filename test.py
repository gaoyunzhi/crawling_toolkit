#coding: utf-8
from getSoup import getSoup
from fetchAlbum import fetchAlbum
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import urllib,os
from sysPath import createPath,combinePath
from PIL import Image, ImageDraw, ImageFont,ImageOps
import os,sys

head='http://hxd.wenming.cn/gxt/'
def test(url):
    urls=[url+'.htm']
    for i in range(2,5):
        urls.append(url+'_'+str(i)+'.htm')
    for url in urls:
        soup=getSoup(url)
        soup=soup.find('div',{'class':"main02cont"})
        for field in soup.findAll('a'):
            link=field['href']
            if link[:4]=='http': continue
            link=head+link
            title=field.findAll(text=True)
            if len(title)!=3: continue
            title=title[2].strip()
            s=getSoup(link)
            s=s.find('div',{'id':'cont'})
            for x in s.findAll('p',{'align':"left"}):
                content=x.find(text=True).strip()
                if content[0].isdigit(): content=content[4:]
                print content
            print '~'*20
            
            

test('http://hxd.wenming.cn/gxt/yryj');