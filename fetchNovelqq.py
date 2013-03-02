#coding: utf-8
import re,urllib
from bs4 import BeautifulSoup,SoupStrainer
from getWebpage import getWebpage
urls=sys.argv[1:]+['http://book.qq.com/s/book/0/24/24822/index.shtml']

def fetch(url):
    index_page=getWebpage(url)
    pass

for url in urls:
    fetch(url)