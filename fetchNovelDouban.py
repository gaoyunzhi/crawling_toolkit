#coding: utf-8
'''
fetch novel from chenlu website
'''

from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import re

def clean(s):
    if '{' in s:
        p=s.find('{')
        q=s.find('}')
        if p<q and q-p<20:
            s=s[:p]+s[q+1:]
    if '【' in s:
        p=s.find('【')
        q=s.find('】')
        if p<q and q-p<40:
            s=s[:p]+s[q+1:] 
    if len(s)<3: return ''       
    return s.strip()
    
def fetch(head):
    prehead='http://book.douban.com/reading/' 
    headP=getWebpage(head)
    soup=BeautifulSoup(headP.decode('utf8','ignore')) 
    t=soup.find('h1')
    title=t.find(text=True)
    soup=soup.find('div',{'id':"content"})
    ans=[]
    for x in soup.findAll('a'):
        if not x.has_key('href'): break
        link=x['href']
        if link[:len(prehead)]!=prehead: continue
        chapter=getWebpage(link)
        chapter=BeautifulSoup(chapter)
        content=chapter.find('div',{'class':"book-content"})
        content='\n'.join(map(clean,content.findAll(text=True)))
        ans.append(content)
    g=open(title+'.txt','w')
    g.write('\n'.join(ans))
    g.close()
        
        
def test():
    fetch(head='http://book.douban.com/subject/20431965/reading')
    
if __name__=='__main__':
    test()