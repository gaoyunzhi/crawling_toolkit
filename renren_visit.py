'''
this program needs to add wait time, may cause problem with your renren id
'''
from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import re
import json,time
from sysPath import createFile

coo='anonymid=h9489u7u-yp0fqs; _r01_=1; mop_uniq_ckid=10.7.18.77_1355594994_642928755; _de=3F3126DBF672F298F26CBA88523C3AB26DEBB8C2103DE356; __utma=151146938.1762808405.1361533510.1361533510.1361533510.1; __utmz=151146938.1361533510.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); l4pager=0; depovince=GW; jebecookies=abb5a061-adf7-4276-9913-0059ed1553e6|||||; p=c506abb8c6dd441921166c4464e116341; ap=269496411; t=351ac721dd34d54a08268e46db838a211; societyguester=351ac721dd34d54a08268e46db838a211; id=269496411; xnsid=cacc7bc0; XNESSESSIONID=376bb17a6b26; at=1; loginfrom=null'
headpage=getWebpage(link='http://friend.renren.com/myfriendlistx.do',
                    cookies=coo)
r=re.search('var friends=(\[.*\]);',headpage)
friendList=r.group(1)
jf=json.loads(friendList)
ids=[]
for f in jf:
    ids.append(f['id'])

timeSleep=1
for id in ids[:]:
    page=getWebpage('http://www.renren.com/'+str(id)+
                    '/profile',
                    cookies=coo,
                    referer='http://www.renren.com/'+str(id)+'/profile#pdetails',
               timeSleep=timeSleep)
    soup=BeautifulSoup(page)
    name=soup.find("title").find(text=True)
    try:
        name=name.split()[2]
    except:
        print name
        print '!!! strange name !!!'
        print 'http://www.renren.com/'+str(id)+'/profile#pdetails'
    
    for x in soup.findAll('a'):
        if not x.has_key("onclick"): continue
        if not  x['onclick'].startswith("showShareFriends"): continue
        num=x.find(text=True)
        num=num.strip("(")
        num=num.strip(")")
        if num.isdigit(): 
            num=int(num)     
            break
    if num<10: print name, 'http://www.renren.com/'+str(id)+'/profile#pdetails'
    