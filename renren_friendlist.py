'''
this program needs to add wait time, may cause problem with your renren id
'''
from getWebpage import getWebpage
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
    