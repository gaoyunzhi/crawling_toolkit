#coding: utf-8
from getSoup import getSoup
from fetchAlbum import fetchAlbum
import os,sys

def fetchInfo(url):
    soup=getSoup(url)
    title=soup.find('title').find(text=True) 
    info=[]
    for img_field in soup.findAll('img'):
        if img_field.has_key('src') and img_field.has_key('alt'):
            name=img_field['alt']
            if len(name)>13 or len(name)<8: continue
            name=img_field.findParent('p').findPreviousSibling('p')
            name=''.join(name.findAll(text=True))
            info.append((name,img_field['src']))
    return (title, info)

            
def fetch(url,numbering=False):
    info=fetchInfo(url)
    fetchAlbum(info,numbering=numbering)

test=['http://gaoyunzhi.wordpress.com/page/1',
      'http://gaoyunzhi.wordpress.com/page/2',]
for url in sys.argv[1:]+test:
    fetch(url,numbering=False)