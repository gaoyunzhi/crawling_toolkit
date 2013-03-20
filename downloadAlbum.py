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
from PIL import Image, ImageDraw, ImageFont,ImageOps
import os,sys

N=18   

def fetchInfo(homeUrl,type=None):
    if 'C:\ '[:-1] in homeUrl:
        f=open(homeUrl)
        homePage=f.read()
        f.close()
    else:
        homePage=getWebpage(homeUrl)
    homeSoup=BeautifulSoup(homePage)
    pageSoup=homeSoup
    info=[]
    if type=='xinmin':    
        album_name=pageSoup.find('title').find(text=True)
        homeUrl=homeUrl.replace('.html','_@@@@.html')
        for x in range(2,100):
            article=pageSoup.find('div',{'class':'article_info'})
            if not article: break
            paragraphs=article.findAll('p')
            if not paragraphs: break
            for paragraph in paragraphs:
                img=paragraph.find('img')
                if not img: 
                    name=paragraph.find(text=True)
                    info.append((name,link))
                else:
                    link=img['src']
            pageUrl=homeUrl.replace('@@@@',str(x))
            page=getWebpage(pageUrl,retry_num=1)
            if not page: break
            pageSoup=BeautifulSoup(page)
        return (album_name,info)
    if type=='douban':
        count=homeSoup.find('span',{'class':'count'})
        if count: 
            count=count.find(text=True)[2:-2]
            count=int(count)
        else:
            count=N # only one page
    ind=len(homeSoup.findAll('h1'))-1
    if ind>1: ind=1
    if type=='douban' or type=='renren':
        album_name=homeSoup.findAll('h1')[ind].find(text=True)
    else:
        album_name=homeSoup.find('title').find(text=True)
    if '-' in album_name:
        if type=='douban' or type=='renren':
            album_name=album_name.split('-')[1]
        else:
            album_name=album_name.split('-')[0]
    album_name=album_name.split()[0]
    album_name=album_name.replace("*",'')
    if album_name=='("▔□▔)/': album_name='smile'
    start=0
    
    
    
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
    
def fetchAlbum((album_name,info),caption=False,type=None):    
    createPath(album_name)
    i=0
    #print len(info)
    for name,url in info:
        i+=1
        ind=name.find('（')
        if ind>1: name=name[:ind]
        cap_content=name
        name=name.replace('/','')
        name=' '.join(name.split())
        name=name.replace(' ','_')   
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
            if type=='douban':
                url=url.replace('large','photo')
            if type=='renren':
                url=url.replace('original','large')
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
            
def fetch(homeUrl,caption):
    type=None
    if 'douban' in homeUrl:
        type='douban'
    if 'renren' in homeUrl or 'a.htm' in homeUrl:
        type='renren'
    if 'xinmin' in homeUrl:
        type='xinmin'
    if 'yahoo' in homeUrl:
        type='yahoo'
        
    info=fetchInfo(homeUrl=homeUrl,type=type)
    fetchAlbum(info,caption,type=type)

    
if __name__=='__main__':
    for x in ['http://www.douban.com/photos/album/78134063/','']+sys.argv[1:]:
        if not x: continue
        fetch(x,caption=False)