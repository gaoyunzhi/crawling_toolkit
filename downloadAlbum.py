#coding: utf-8
'''
download album for douban, will extend to other website/application. This time, 
I will try to write all album downloading code in one file (or much few files than what 
I did to novel fetching...)

'''

from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import urllib,os
from sysPath import createPath,combinePath
from PIL import Image, ImageDraw, ImageFont
import os,sys

N=18   

def fetchInfo(homeUrl,type=None):
    homePage=getWebpage(homeUrl)
    homeSoup=BeautifulSoup(homePage)
    if type=='douban':
        count=homeSoup.find('span',{'class':'count'})
        if count: 
            count=count.find(text=True)[2:-2]
            count=int(count)
        else:
            count=N # only one page
    album_name=homeSoup.findAll('h1')[-1].find(text=True)
    if '-' in album_name:
        album_name=album_name.split('-')[1]
    album_name=album_name.split()[0]
    start=0
    pageSoup=homeSoup
    info=[]
    
    if type=='douban':
        while True:
            photos=pageSoup.findAll('div',{'class':'photo_wrap'})
            if len(photos)>N: print 'warning on photo number!'
            for photo in photos:
                aTag=photo.find('a',{'class':"photolst_photo"})
                if not aTag: continue
                name=aTag['title']
                url=photo.find('img')['src']
                url=url.replace('thumb','large')
                info.append((name,url))
            start+=N
            if start>count: break
            page=getWebpage(homeUrl+'?start='+str(start))
            pageSoup=BeautifulSoup(page)
    
    photos=homeSoup.findAll('span',{'class':"img"})
    for photo in photos:
        img=photo.find('img')
        if not img: continue
        if not img.has_key('alt'): continue
        name=img['alt']
        url=img['src']
        url=url.replace('head','original')
        info.append((name,url))
        
    return (album_name,info)
    
def fetchAlbum((album_name,info),caption=False):    
    createPath(album_name)
    i=0
    for name,url in info:
        i+=1
        cap_content=name
        name=name.replace('/','')
        name=' '.join(name.split())
        name=name.replace(' ','_')
        name=combinePath(album_name,str(i)+'_'+name)+'.jpg'        
        try:
            urllib.urlretrieve(url,name)
        except:
            print url,name
            continue
        if os.stat(name).st_size<1000:
            url=url.replace('large','photo')
            urllib.urlretrieve(url,name)
        if caption:
            im = Image.open(name)
            d = ImageDraw.Draw(im)
            w,h = im.size    
            f=ImageFont.truetype('C:\Windows\Fonts\simsun.ttc',24)     
            d.text((4,h-24), cap_content,font=f,fill="blue")
            im.save(name)
            
def fetch(homeUrl,caption):
    type=None
    if 'douban' in homeUrl:
        type='douban'
    if 'renren' in homeUrl:
        type='renren'
        
    info=fetchInfo(homeUrl=homeUrl,type=type)
    fetchAlbum(info,caption)

    
if __name__=='__main__':
    for x in ['',
              '']+sys.argv[1:]:
        if not x: continue
        fetch(x,caption=True)