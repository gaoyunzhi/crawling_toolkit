'''
this program needs to add wait time, may cause problem with your renren id
'''
from getWebpage import getWebpage
import re
import json

coo='anonymid=h9489u7u-yp0fqs; _r01_=1; l4pager=1; depovince=GW; __utma=151146938.281202775.1355493087.1355493087.1355581819.2; __utmz=151146938.1355581819.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/pages/autoLogin-ads.jsp; _de=3F3126DBF672F298F26CBA88523C3AB26DEBB8C2103DE356; jebecookies=f4c58476-61b0-4d1b-9841-8539844085e8|||||; p=c003d894128f49993145f4e49afb76c41; ap=269496411; JSESSIONID=abc9ahqrKm-dYgIaZFFUt; t=49a74cd11e44ffe25866742204c284cb1; societyguester=49a74cd11e44ffe25866742204c284cb1; id=269496411; xnsid=6080bc05; loginfrom=null; feedType=269496411_hot; vip=1'
headpage=getWebpage(link='http://friend.renren.com/myfriendlistx.do',
                    cookies=coo)
r=re.search('var friends=(\[.*\]);',headpage)
friendList=r.group(1)
jf=json.loads(friendList)
ids=[]
for f in jf:
    ids.append(f['id'])
for id in ids[-100:]:
    timeSleep=5
    print id
    getWebpage('http://www.renren.com/'+str(id)+'/profile',cookies=coo,read=False)
    