#coding: utf-8
import urllib,os
from sysPath import createPath,combinePath
from PIL import Image, ImageDraw, ImageFont,ImageOps
def fetchAlbum((album_name,info),caption=False,type=None):    
    createPath(album_name)
    i=0
    for name,url in info:
        i+=1
        ind=name.find('（')
        if ind>1: name=name[:ind]
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
            if type=='douban':
                url=url.replace('large','photo')
            if type=='renren':
                url=url.replace('original','large')
            urllib.urlretrieve(url,name)
        if caption:
            im = Image.open(name)
            w,h = im.size
            new_im = Image.new("RGB", (w,h+24))
            new_im.paste(im,(0,0))                
            f=ImageFont.truetype('C:\Windows\Fonts\simsun.ttc',24)   
            d = ImageDraw.Draw(new_im)
            d.text((4,h), cap_content,font=f,fill="white")
            new_im.save(name)