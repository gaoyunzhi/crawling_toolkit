#coding: utf-8
'''
我终于想明白了，文件还是分开来的好。
'''
from getSoup import getSoup
from soupToTxt import soupToTxt
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import sys
N=100
M=25 


def fetchInfo(url):
    filename=''
    info=[]
    for n in xrange(N):        
        soup=getSoup(url+'?start='+str(M*n))
        if not filename: filename=soup.find('title').find(text=True)
        titles=soup.findAll('div',{'class':"title"})
        if not titles: break # no more
        for title in titles:
            link=title.find('a')
            info.append((link['href'],link.find(text=True).strip()))
    return (filename,info)

def fetchNote((filename,info)):
    ans=[]
    for url, name in info:
        soup=getSoup(url)
        note=soup.find('div',{'class':'note-content'})
        if not note:
            note=soup.find('div',{'class':'note','id':"link-report"})
        ans.append(soupToTxt(note,title=name))
    f=open(filename+'.txt','w')
    f.write(('\n\n\n\n'+'-'*30+'\n\n').join(ans))
    f.close()
        
    









def fetch(url):
    info=fetchInfo(url)
    fetchNote(info)

if __name__=='__main__':
    test=['http://www.douban.com/doulist/1811798/',
          'http://www.douban.com/doulist/1781546/',
          'http://www.douban.com/doulist/1783020/']
    for url in sys.argv[1:]+test:
        fetch(url)