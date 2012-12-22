'''
this program needs to add wait time, may cause problem with your renren id
'''
from getWebpage import getWebpage
import re
import json,time
from sysPath import createFile,sysPath
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs

coo='datr=1HSWUNG14Cr81JphyUZWTl2i; lu=gAff9sJJ2_wuev5W3zxFsGZA; sub=128; p=49; c_user=1216615221; csm=2; fr=0regP7HiBNucJQa1n.AWVfvGNhos7mlakT0e52olU2aWo.BQlnT_.nT.AWVtovRV; s=Aa7LrP8dIAOi4SoX; xs=3%3ArXa_AglvHBTByg%3A2%3A1352037631; act=1356128659553%2F6%3A2; presence=EM356128936EuserFA21216615221A2EstateFDsb2F0Et2F_5b_5dElm2FnullEuct2F135610056B0EtrFA2loadA2EtwF1698182903EatF1356128697024G356128936322CEchFDp_5f1216615221F8CC; wd=1280x299'
f=open(sysPath('webpages/ids.txt'))
jf=json.loads(f.read().decode('utf8','ignore'))
f.close()

createFile('infos_fb.txt',force=True)
g=open('infos_fb.txt','a')
g.write('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Group Membership,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 - Type,E-mail 2 - Value,Phone 1 - Type,Phone 1 - Value'+'\n')
g.close()

ans=[]
for f in jf['data']:
    info=getWebpage('http://www.facebook.com/'+str(f['id']),
                    cookies=coo,
                    info=str(f['id'])
                    )
    bI=BeautifulSoup(info)
    link=bI.find('link',{'rel':'alternate'})
    '''
    info=getWebpage(link['href']+'/info',
                    cookies=coo,
                    info=str(f['id'])
                    )
    '''
    ind=link['href'].rfind('/')
    email=link['href'][ind+1:]
    ans.append((f['name'],f['id'],email+'@facebook.com'))
    name=f['name']
    id=f['id']
    email=email+'@facebook.com'
    if email[:7]=='profile':
        email=id+'@facebook.com'
    g=open('infos_fb.txt','a')
    g.write(name)
    g.write(','+name)
    g.write(',,,,,,,,,,,,,,,,,,,,,,,,'+id+',,,'+email+',,'+''+',,'+''+'\n')
    g.close()
    

print 'over'
