#coding: utf-8
'''
fetch novel from douban reading website
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
    coo='bid="yrdz0J5ispI"; __gads=ID=720d3fea3d3fb612:T=1352676703:S=ALNI_MZ72ae6zGEgpSfYlI_B0WyhBlV-zA; ll="0"; viewed="2052978_11584608"; dbcl2="4898454:5qnPL5l4FFw"; ck="3bMe"; __utma=30149280.1032140921.1356576933.1356576933.1356614007.2; __utmc=30149280; __utmz=30149280.1356576933.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=30149280.489'
    parts=head.split('/')
    ref='/'.join(parts[:-3])
    headP=getWebpage('http://read.douban.com/reader/',cookies='hst=1; '+coo, reLoad=True,referer=ref)
    return
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
    fetch(head='http://read.douban.com/reader/ebook/450696/page/2/')
    
if __name__=='__main__':
    test()