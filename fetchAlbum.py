#coding: utf-8
import urllib,os,re
def filename(s):
    return re.sub(r"[\/\\\:\*\?\"\<\>\|]", "",s)   
    
def fetchAlbum((album_name,info),type=None,numbering=False):   
    album_name=filename(album_name).strip().split()[0] 
    if not os.path.exists(album_name):
        os.makedirs(album_name)
    i=0
    for name,url in info:
        i+=1
        name=filename(name) 
        if not name: 
            name=str(i) 
        elif numbering:
            name=str(i)+'_'+name 
        name=os.path.join(album_name,name)+'.jpg'        
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