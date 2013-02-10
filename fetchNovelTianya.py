#coding: utf-8
'''
fetch novel from tianya
'''

from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import re,urllib

def clean(s):
    return s.strip()
    
def fetch(prefix,suffix='.shtml'):
    prefaceP=getWebpage(prefix+'1'+suffix)
    prefaceS=BeautifulSoup(prefaceP.decode('utf8','ignore'))
    book_title=prefaceS.find('title').find(text=True)
    num_page=prefaceS.find('div',{'class':"atl-pages"}).find('form')['onsubmit']
    num_page=num_page.split()[-1]
    num_page=num_page.split(',')[-1]
    num_page=num_page.split(')')[0]
    num_page=int(num_page)
    book_author=prefaceS.find('a',{'replyid':0})['author']
    ans=[]
    last_author=book_author
    for page_num in xrange(1,num_page):
        link=prefix+str(page_num)+suffix
        page=getWebpage(link)
        soup=BeautifulSoup(page.decode('utf8','ignore'))
        posts=soup.findAll('div',{'class':"atl-item"})
        for post in posts:
            try:
                author=post.find('div',{'class':"atl-info"}).find('a',{'target':"_blank"})['uname']
            except:
                author=''
            if author==last_author and author!='': 
                author=''
            else:
                last_author=author
            try:
                post=post.find('div',{'class':"bbs-content"})  
            except:
                pass 
            post='\n'.join(map(clean,post.findAll(text=True)))
            if len(post)<30: continue
            if author!='': post=u'作者：'+author+'\n'+post
            post.replace('\n\n','\n')
            post.replace('\n\n','\n')
            ans.append(post)
    g=open(book_title+'.txt','w')
    g.write('\n\n'.join(ans))
    g.close()
 
        
def test():
    fetch(prefix='http://bbs.tianya.cn/post-no05-120045-',suffix='.shtml')
    
if __name__=='__main__':
    test()