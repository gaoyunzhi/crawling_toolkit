'''
this program needs to add wait time, may cause problem with your renren id
'''
from getWebpage import getWebpage
import re
import json,time
from sysPath import createFile

coo='anonymid=h9489u7u-yp0fqs; _r01_=1; l4pager=1; mop_uniq_ckid=10.7.18.77_1355594994_642928755; __utma=151146938.281202775.1355493087.1355581819.1355833127.3; __utmz=151146938.1355833127.3.3.utmcsr=notify.renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/rmessage/rmessage-apply.html; _de=3F3126DBF672F298F26CBA88523C3AB26DEBB8C2103DE356; depovince=GW; jebecookies=a257a988-6f54-4d1d-9be2-8391040f201d|||||; p=c003d894128f49993145f4e49afb76c41; ap=269496411; JSESSIONID=abchtgHWRNjrX9SRIQWVt; t=c833ebb11ba4a5f8f026f6df4489ef601; societyguester=c833ebb11ba4a5f8f026f6df4489ef601; id=269496411; xnsid=f55bd7c; loginfrom=null; feedType=269496411_hot; vip=1'
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
    getWebpage('http://www.renren.com/'+str(id)+
                    '/profile?v=info_ajax&undefined',
                    cookies=coo,
                    referer='http://www.renren.com/'+str(id)+'/profile#pdetails',
               timeSleep=timeSleep,read=False)
    print id
    