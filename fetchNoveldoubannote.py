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
    return s.strip()
    
def fetch(head):
    headP=getWebpage(head)
    soup=BeautifulSoup(headP.decode('utf8','ignore'))
    t=soup.find('h1')
    title=t.find(text=True)
    ans=[]
    for i in xrange(0,10000,10):
        link=head+'?start='+str(i)
        page=getWebpage(link)
        soup=BeautifulSoup(page)
        notes=[]
        for x in soup.findAll('span',{'class':'rec'}):
            if not x.has_key('id') : continue
            if  x['id'][:5]!='Note-': continue
            notes.append(x['id'][5:])
        if notes==[]: break
        for note in notes:
            page=getWebpage('http://www.douban.com/note/'+note)
            soup=BeautifulSoup(page)
            note_title=soup.find('title').find(text=True)
            article=soup.find('div',{'class':"note", 'id':"link-report"})
            content=note_title+'\n'.join(map(clean,article.findAll(text=True)))+'\n\n'
            ans.append(content)
 
    g=open(title+'.txt','w')
    g.write('\n'.join(ans))
    g.close()
        
        
def test():
    fetch(head='http://www.douban.com/people/zhangjiawei/notes')
    
if __name__=='__main__':
    test()