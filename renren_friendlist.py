'''
this program needs to add wait time, may cause problem with your renren id
'''
from getWebpage import getWebpage
import re
import json

coo='anonymid=h9489u7u-yp0fqs; _r01_=1; l4pager=1; __utma=10481322.2138789767.1353121296.1353121296.1353121296.1; __utmz=10481322.1353121296.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/269496411; _de=3F3126DBF672F298F26CBA88523C3AB26DEBB8C2103DE356; depovince=GW; jebecookies=01a4c4c3-fb2e-4246-9360-794ad4ec02f3|||||; p=8793ab004461daa321fb9fa47a2c26621; ap=269496411; t=bb74f02157a487d6577623227322a3ad1; societyguester=bb74f02157a487d6577623227322a3ad1; id=269496411; xnsid=668daff8; loginfrom=null; JSESSIONID=9E173174EA0F90DED46F7C68F99CDFC8'
headpage=getWebpage(link='http://friend.renren.com/myfriendlistx.do',
                    cookies=coo)
r=re.search('var friends=(\[.*\]);',headpage)
friendList=r.group(1)
jf=json.loads(friendList)
ids=[]
for f in jf:
    ids.append(f['id'])
for id in ids[20:]:
    getWebpage('http://www.renren.com/'+str(id)+'/profile',cookies=coo,read=False)
    