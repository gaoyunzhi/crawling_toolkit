#coding: utf-8
'''
fetch novel for several website

我是一个二货
'''

from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import re,urllib,sys

def fetchTieba(prefaceL,lz=True):#lz, only see the top floor poster
    if lz and prefaceL[-8:]!='see_lz=1': prefaceL+='?see_lz=1'    
    prefaceP=getWebpage(prefaceL)
    prefaceS=BeautifulSoup(prefaceP.decode('gbk','ignore'))
    book_title=prefaceS.find('title').find(text=True)
    for link in prefaceS.findAll('a'):
        if link.find(text=True)=='尾页':
            lastL=link['href']
            ind=lastL.rfind('=')
            totalP=int(lastL[ind+1:])
    pageS=prefaceS
    currentP=1
    if not '?' in prefaceL: 
        prefaceL+='?'
    else:
        prefaceL+='&'
    ans=[]
    while True:
        posts=pageS.findAll('div',{'class':"d_post_content"})
        for post in posts:
            ans.append('\n'.join(post.findAll(text=True)))
        currentP+=1
        if currentP>totalP: break
        page=getWebpage(prefaceL+'pn='+str(currentP))
        pageS=BeautifulSoup(page) 
    g=open(book_title+'.txt','w')
    g.write('\n\n'.join(ans))
    g.close()
 
        
def fetch(job):
    if 'tieba' in job:
        fetchTieba(job)
    else:
        print job+' has not corresponding fetch code'
    
if __name__=='__main__':
    jobs=sys.argv[1:]
    jobs+=['http://tieba.baidu.com/p/2034339902']
    for job in jobs:
        if not job: continue
        fetch(job)