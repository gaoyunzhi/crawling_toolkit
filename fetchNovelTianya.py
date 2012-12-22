#coding: utf-8
'''
fetch novel from tianya yidu
'''

from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import re

def clean(s):
    return s.strip()
    
def fetch(head,nid):
    head+='-'+str(nid)
    headP=getWebpage(head+'.html')
    soup=BeautifulSoup(headP.decode('utf8','ignore'))
    n=soup.find('div',{'class':"pageNum1"})
    n=n.contents[0]
    r=re.match(u'共'+'(\d*)'+u'页',n)
    n=r.group(1)
    try:
        n=int(n)
    except:
        print 'failed to find the number of page'
        n=1000
    ans=[]
    for i in range(1,n+1):
        page=head+'-'+str(i)+'.html'
        page=getWebpage(page)
        soup=BeautifulSoup(page)
        posts=soup.findAll('li',{'class':'at c h2'})
        for post in posts:
            post='\n'.join(map(clean,post.findAll(text=True)))
            if len(post)<10: continue
            ans.append(post)
    g=open(str(nid)+'.txt','w')
    g.write('\n'.join(ans))
    g.close()
    
    return
   

    
    
    return
    chapters=extractLinks(link=link, requireLinkStart=link,avoidKeys=['img','alt','src'],requireLinkEnd='.html')
    print chapters
    content=getWebpage(link)
    soup=BeautifulSoup(content)
    paras=soup.findAll('div',{'class':'paragraph'})
    intro=soup.find('div',{'class':'bookintro'})
    book_name=soup.find('div',{'id':'book-cover'}).find('a')['title']
    print 'collecting: ',book_name
    f=open(book_name+'.txt','w')
    f.write('intro: ')
    for y in intro.findAll(text=True):
        if y.encode('utf8','ignore').strip()=='': continue
        f.write(y.encode('utf8','ignore')+'\n')
    for x in paras:
        for y in x.findAll(text=True):
            f.write(y.encode('utf8','ignore')+'\n')
    f.close()
    start=int(chapters[0]['href'][len(link):-5])
    end=int(chapters[-1]['href'][len(link):-5])+20
    chapterD={}
    for x in chapters:
        num=int(x['href'][len(link):-5])
        title=x['title']
        chapterD[num]=title
    count=0
    for i in range(start,end):
        chapter=link+str(i)+'.html'
        content=getWebpage(chapter)
        soup=BeautifulSoup(content)
        content=soup.find('div',{'id':'zoom'}) 
        f=open(book_name+'.txt','a')
        if i in chapterD:
            f.write('\n\n'+chapterD[i].encode('utf8','ignore')+'\n')
        if content==None: continue
        for y in content.findAll(text=True):
            if y.encode('utf8','ignore').strip()=='': continue
            f.write(y.encode('utf8','ignore')+'\n')
        f.close()
        #if count>5:break
        count+=1
        
        
def test():
    fetch(head='http://www.tianyayidu.com/article',nid=482520)
    
if __name__=='__main__':
    test()