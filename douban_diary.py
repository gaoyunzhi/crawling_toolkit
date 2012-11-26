import urllib,urllib2,codecs,urlparse
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
# -*- coding:utf8 -*-
def diary(title,content):
    link='http://www.douban.com/note/create'
    cookies='''ck="3bMe"; __utmc=30149280; bid="cwoRAvJOWdQ"; dbcl2="4898454:5qnPL5l4FFw"; __utma=30149280.127203582.1353697363.1353697363.1353697363.1; __utmb=30149280.4.10.1353697363; __utmz=30149280.1353697363.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.489'''
    page_info = urllib2.build_opener()
    page_info.addheaders.append(('Cookie', cookies))
    postDict={}
    req = urllib2.Request(link);
    page=page_info.open(req)
    soup=BeautifulSoup(page.read())
    add=soup.find('input',{'type':"hidden",'id':"note_id", 'name':"note_id"})['value']
    postData='ck=3bMe&note_id='+add+'&note_title='+title+'&note_text='+content+'&note_privacy=P&note_submit=%E5%8F%91%E8%A1%A8'
    req = urllib2.Request(link,postData);
    page_info.open(req)

diary('test_title_python_1','test_content_python_1')
