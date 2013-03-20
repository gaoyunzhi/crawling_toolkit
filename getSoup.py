from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs

def getSoup(url,encode='utf8',coo=''):
    page=getWebpage(url,cookies=coo)
    return BeautifulSoup(page.decode(encode,'ignore'))