# for sina
#coding: utf-8
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
from getWebpage import getWebpage # get the local fname of a webpage
from sysPath import folderPath
from getDetails import getDetails
from extractLinks import extractLinks
from getWebpage import getWebpage

def fetchNovel(link, rLS=None):
    if rLS==None: rLS=link
    chapters=extractLinks(link=link, requireLinkStart=rLS,avoidKeys=['img','alt','src'],\
                          requireLinkEnd='.html')
    content=getWebpage(link)
    soup=BeautifulSoup(content)
    book_name=''.join(soup.find('title').contents)
    book_name=book_name.split('_')[0]
    print 'collecting: ',book_name
    f=open(book_name+'.txt','w')
    f.close()
    count=0
    for x in chapters:
        chapter='http://data.book.163.com'+x['href']
        #print chapter,'0'
        content=getWebpage(chapter)
        soup=BeautifulSoup(content)
        content=soup.find('div',{'class':'bk-article-body','id':'bk-article-body'})
        f=open(book_name+'.txt','a')
        #print chapter,'1'
        try:
            title=''.join(x.contents).encode('GBK','ignore')
        except:
            title=''
        if title!='' and (title[-1]!=')' or title[-3:]=='(1)'):f.write('\n\n'+title+'\n')
        #print chapter,'2'
        for y in content.findAll(text=True):
            if y.encode('GBK','ignore').strip()=='': continue
            f.write(y.encode('GBK','ignore')+'\n')
        f.close()
        #if count>5:break
        count+=1

link='http://data.book.163.com/book/home/009200190001/000BOKdL.html'
rLS='/book/section/000BOKdL/000BOKdL'
fetchNovel(link,rLS=rLS)
