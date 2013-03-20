#coding: utf-8
from getSoup import getSoup
from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import urllib,os
from sysPath import createPath,combinePath
from PIL import Image, ImageDraw, ImageFont,ImageOps
import os,sys

N=18   

def fetchInfo(homeUrl,type=None):
    homeSoup=getSoup(homeUrl)
    pageSoup=homeSoup
    info=[]
    count=homeSoup.find('span',{'class':'count'})
    if count: 
        count=count.find(text=True)[2:-2]
        count=int(count)
    else:
        count=N # only one page
    ind=len(homeSoup.findAll('h1'))-1
    if ind>1: ind=1
    album_name=homeSoup.findAll('h1')[ind].find(text=True)
    if '-' in album_name:
        album_name=album_name.split('-')[1]
    album_name=album_name.replace("*",'')
    album_name=album_name.replace("/",'')
    album_name=album_name.split()[0]    
    start=0
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
    if not photos: 
        photos=homeSoup.findAll('a',{'class':"pic"})
    for photo in photos:
        img=photo.find('img')
        if not img: continue
        if not img.has_key('alt'): continue
        name=img['alt']
        if img.has_key('data-src'): 
            url=img['data-src']
        else:
            url=img['src']
        url=url.replace('head','original')
        info.append((url,name))    
    return (album_name,info)
    
def fetchAlbum((album_name,info),caption=False,type=None,simple_name=False):    
    createPath(album_name)
    i=0
    for name,url in info:
        i+=1
        ind=name.find(u'（')
        if ind>1: name=name[:ind]
        cap_content=name
        name=name.replace('/','')
        name=' '.join(name.split())
        name=name.replace(' ','_')   
        if simple_name:name=''
        if name!='':
            fname=str(i)+'_'+name  
        else:
            fname=str(i)            
        name=combinePath(album_name,fname)+'.jpg'            
        try:
            urllib.urlretrieve(url,name)
        except:
            print url,name
            continue
        if os.stat(name).st_size<1000:
            url=url.replace('large','photo')
            try:
                urllib.urlretrieve(url,name)
            except:
                print url, name
                continue
        if caption and cap_content:
            im = Image.open(name)
            w,h = im.size
            new_im = Image.new("RGB", (w,h+24))
            new_im.paste(im,(0,0))                
            f=ImageFont.truetype('C:\Windows\Fonts\simsun.ttc',24)   
            d = ImageDraw.Draw(new_im)
            d.text((4,h), cap_content,font=f,fill="white")
            new_im.save(name)
            
def fetch(homeUrl,caption,simple_name=False):   
    info=fetchInfo(homeUrl=homeUrl)
    fetchAlbum(info,caption,simple_name=simple_name)

    
for x in ['','']+sys.argv[1:]:
    if not x: continue
    fetch(x,caption=False)
