#coding: utf-8
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
    
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

def soupToTxt(soup,title=''):
    content=title+'\n'+'\n'.join(map(clean,soup.findAll(text=True)))
    return content
    
    