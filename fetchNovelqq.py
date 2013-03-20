#coding: utf-8
import sys
from getSoup import getSoup
from soupToTxt import soupToTxt
urls=sys.argv[1:]+['http://book.qq.com/s/book/0/26/26248/index.shtml','http://book.qq.com/s/book/0/26/26830/index.shtml']
Ch_Start="javascript:opennew('http://book.qq.com"

def title_clean(x):
    x=x.strip()
    i=x.find('：')
    if 0<=i<=len(x)-5:x=x[i+1:]
    if x[-1]==')':
        i=x.rfind('(')
        return x[:i]
    return x

def fetch_book(info):
    book_title=info.next()
    old_title=''
    content=[]
    for url,ch_title in info:
        if ch_title==old_title:
            ch_title=''
        else:
            old_title=ch_title
        ch=getSoup(url,encode='gbk').find('div',{'id':"content"})
        content.append(soupToTxt(ch,title=ch_title))
    f=open(book_title+'.txt','w')
    f.write(''.join(content))
    f.close()
        
    
def get_info(url):
    index_page=getSoup(url,encode='gbk')
    book_title=index_page.find('title').find(text=True)[:-10]
    yield book_title
    for ch in index_page.findAll('a'):
        if not ch.has_key('href') or not ch['href'].startswith(Ch_Start): continue 
        ch_url=ch['href'][20:-2]
        ch_title=title_clean(ch.find(text=True))
        yield ch_url,ch_title
        
def fetch(url):
    info=get_info(url)
    fetch_book(info)
for url in urls:
    fetch(url)