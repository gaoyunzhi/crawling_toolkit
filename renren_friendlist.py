'''
this program needs to add wait time, may cause problem with your renren id
'''
from getWebpage import getWebpage
import re
import json,time
from sysPath import createFile

coo='anonymid=h9489u7u-yp0fqs; _r01_=1; l4pager=1; depovince=GW; __utma=151146938.281202775.1355493087.1355493087.1355581819.2; __utmz=151146938.1355581819.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/pages/autoLogin-ads.jsp; _de=3F3126DBF672F298F26CBA88523C3AB26DEBB8C2103DE356; jebecookies=f4c58476-61b0-4d1b-9841-8539844085e8|||||; p=c003d894128f49993145f4e49afb76c41; ap=269496411; JSESSIONID=abc9ahqrKm-dYgIaZFFUt; t=49a74cd11e44ffe25866742204c284cb1; societyguester=49a74cd11e44ffe25866742204c284cb1; id=269496411; xnsid=6080bc05; loginfrom=null; feedType=269496411_hot; vip=1'
headpage=getWebpage(link='http://friend.renren.com/myfriendlistx.do',
                    cookies=coo)
r=re.search('var friends=(\[.*\]);',headpage)
friendList=r.group(1)
jf=json.loads(friendList)
ids=[]
for f in jf:
    ids.append(f['id'])
createFile('infos.txt',force=True)
g=open('infos.txt','a')
g.write('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Group Membership,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 - Type,E-mail 2 - Value,Phone 1 - Type,Phone 1 - Value'+'\n')
g.close()

count=0
for id in ids[:]:
    timeSleep=1
    count+=1
    #print count

    mainInfo=getWebpage('http://www.renren.com/'+str(id)+
                    '/profile?v=info_ajax&undefined',
                    cookies=coo,
                    referer='http://www.renren.com/'+str(id)+'/profile#pdetails',
               timeSleep=timeSleep,info=str(id))
    s=re.search('ajaxDelFriend\('+str(id)+",'(.*)",mainInfo)
    try:
        name=s.group(1)
    except:
        try:
            s=re.search('talkto\('+str(id)+", '(.*)",mainInfo)
            name=s.group(1)
        except:
            print id
            print mainInfo
    ind=name.find("'")
    name=name[:ind]
    

    contactInfo=getWebpage('http://friend.renren.com/getprofilecontact/'+str(id),
                    cookies=coo,
                    timeSleep=timeSleep,
                    info=str(id))
    contactInfo=json.loads(contactInfo)
    try:
        msn=contactInfo['msn']
    except:
        msn=''
    try:
        qq=contactInfo['qq']+'@qq.com'
        if qq=='0@qq.com': qq=''
    except:
        qq=''
    try:
        mobile='01186'+contactInfo['mobile']
    except:
        mobile=''
    infos=[name,msn,qq,mobile]
    g=open('infos.txt','a')
    g.write(name)
    g.write(','+name)
    g.write(',,,,,,,,,,,,,,,,,,,,,,,,,,,'+qq+',,'+msn+',,'+mobile+'\n')
    g.close()
print 'over'
    