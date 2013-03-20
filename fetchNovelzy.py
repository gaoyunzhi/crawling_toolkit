#coding: utf-8
'''
fetch novel from website
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
    s=s.replace('-','')     
    return s.strip()
    
def fetch(head):
    headP=getWebpage(head)
    soup=BeautifulSoup(headP.decode('gbk','ignore'))
    t=soup.find('h1')
    title=t.find(text=True)
    ans=[]
    for x in soup.findAll('td',{'class':"ccss"})[90:]:
        link=x.find('a')
        if link==None: continue
        if not link.has_key('href'): continue
        link=head+link['href']
        chapter=getWebpage(link)
        chapter=BeautifulSoup(chapter)
        content=chapter.find('div',{'id':"content"})
        content='\n'.join(map(clean,content.findAll(text=True)))
        ans.append(content)
    g=open(title+'.txt','w')
    g.write('\n'.join(ans))
    g.close()
        
def test():
    fetch(head='http://www.zybook.net/html/30/30510/')
    
if __name__=='__main__':
    test()