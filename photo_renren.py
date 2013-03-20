#coding: utf-8
from getSoup import getSoup
from fetchAlbum import fetchAlbum
import os,sys

coo='anonymid=h9489u7u-yp0fqs; _r01_=1; mop_uniq_ckid=10.7.18.77_1355594994_642928755; l4pager=0; depovince=GW; _de=3F3126DBF672F298F26CBA88523C3AB26DEBB8C2103DE356; p=9babffa88c9c71f7219d11a49178460d1; ap=269496411; t=a69a7611e5d417bd2226b2f0d57e652e1; societyguester=a69a7611e5d417bd2226b2f0d57e652e1; id=269496411; xnsid=815e175e; XNESSESSIONID=9adfd23b1dae; IL_D=2; at=1; __utma=10481322.145044192.1363634540.1363634540.1363636668.2; __utmb=10481322.4.10.1363636668; __utmc=10481322; __utmz=10481322.1363636668.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/269496411; loginfrom=null; vip=1'

def fetchInfo(url):
    soup=getSoup(url,coo=coo)
    title=soup.find('title').find(text=True).split()[-1] 
    info=[]
    for img_field in soup.findAll('a',{'class':"pic"}):
        img=img_field.find('img')
        if not img: continue
        if not img.has_key('alt'): continue
        name=img['alt']
        if img.has_key('data-src'): 
            url=img['data-src']
        else:
            url=img['src']
        url=url.replace('head','original')
        info.append((name,url))
    return (title, info)

            
def fetch(url,numbering=False):
    info=fetchInfo(url)
    fetchAlbum(info,numbering=numbering)

test=['http://photo.renren.com/photo/319282875/album-362213591']
for url in sys.argv[1:]+test:
    fetch(url,numbering=True)