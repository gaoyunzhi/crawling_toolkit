#coding: utf-8
from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
from sysPath import createFile
    
def forum_crawl(link,outFile):
    createFile(outFile, force=True)
    p=1
    lastpage=''
    while True:            
        page=getWebpage(link+str(p),timeSleep=0)
        if not page or page==lastpage: break
        lastpage=page
        soup=BeautifulSoup(page.decode('gb2312','ignore'))
        fields=soup.findAll('div',{'id':"content"})
        for f in fields:
            for line in f.findAll(text=True):
                if len(line.strip())>1:
                    f=open(outFile,'a')
                    f.write(line)
                    f.close() 
        p+=1
        
        

if __name__=='__main__':
    head='http://www.hzfj.org/archiver/?tid-95690.html&page='
    outFile=u'五灯会元白话.txt'
    forum_crawl(head,outFile)