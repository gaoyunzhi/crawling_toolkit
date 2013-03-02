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

def fetchInfo(url):
    soup=getSoup(url)
    title=soup.find('title').find(text=True)
    soup=soup.find('div',{'class':'note-content'})    
    info=[]
    for img_field in soup.findAll('img'):
        if img_field.has_key('src') and img_field.has_key('alt'):
            info.append((img_field['alt'],img_field['src']))
    return (title, info)

            
def fetch(url):
    info=fetchInfo(url)
    fetchAlbum(info,caption=caption)

if __name__=='__main__':
    global caption
    caption=True
    test=['http://site.douban.com/108849/widget/notes/217228/note/104182566/']
    for url in sys.argv[1:]+test:
        fetch(url)