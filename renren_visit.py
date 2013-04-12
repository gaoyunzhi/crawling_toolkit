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
import sys

coo='''anonymid=h9489u7u-yp0fqs; _r01_=1; mop_uniq_ckid=10.7.18.77_1355594994_642928755; __utma=10481322.145044192.1363634540.1363634540.1363636668.2; __utmz=10481322.1363636668.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/269496411; _de=3F3126DBF672F298F26CBA88523C3AB26DEBB8C2103DE356; depovince=GW; bt_new=12; jebecookies=63880745-b57f-4dce-b75e-7cc2218be89a|||||; p=9babffa88c9c71f7219d11a49178460d1; ap=269496411; t=fa5d5d911dc472ebde86481e5486062e1; societyguester=fa5d5d911dc472ebde86481e5486062e1; id=269496411; xnsid=6ef4dee; loginfrom=null; feedType=269496411_hot; JSESSIONID=abcMqcp8dHsTAh3nle53t; l4pager=0'''
headpage=getWebpage(link='http://friend.renren.com/myfriendlistx.do',
                    cookies=coo)
r=re.search('var friends=(\[.*\]);',headpage)
friendList=r.group(1)
jf=json.loads(friendList)
ids=[]
for f in jf:
    ids.append(f['id'])

if len(sys.argv)>=2:
    start_num=int(sys.argv[1])
else:
    start_num=0

timeSleep=0.8
for id in ids[start_num:start_num+100]:
    page=getWebpage('http://www.renren.com/'+str(id)+
                    '/profile',
                    cookies=coo,
                    referer='http://www.renren.com/'+str(id)+'/profile#pdetails',
               timeSleep=timeSleep,read=False)
   
