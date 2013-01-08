'''
fetch novel from safariread
'''

from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import re,json

coo='Safari=cookieversion=2&cookie-monster=true&portal=proquest&key=6F22101170B7A1537D2DF19298E579F3E2C72A7FD2CE88FF72CFA4E025B017CD6027815DAC0CC9801517BAF70B15961AEE65512F644B6E9F92B6A87CB6B96E2B53E76E50409424974917F1EF2732570DFF82193809A41169BBC4CB6C563477C640AB2AAADDBBC893C4CE0FF41D5F8369B62F9A7EA5667381757565FB&sessionid=bb6adf19-b555-4f54-8222-f50f66405686&ref=Undefined&logged=true; Path=/; Domain=proquest.safaribooksonline.com'
def clean(s):
    return s.strip()

def reply(s):
    m=re.search('--------',s)
    if m==None: 
        return False
    return True

def toId(s):
    return s[3:-1]
    
    
def fetch(head):
    headP=getWebpage(head+'firstchapter')
    soup=BeautifulSoup(headP)
    for f in soup.findAll('input'):
        if not f.has_key('value'): continue
        if len(f['value'])<100: continue
        break
    ids=re.findall("'id\d*'",f['value'])
    ids=map(toId,ids)
    
    ans=[]
    for id in ids:
        try:
            page=head+'id'+id
            page=getWebpage(page,timeSleep=10) 
            soup=BeautifulSoup(page)
            content=soup.find('div',{'class':"htmlcontent"})
            content=''.join(map(clean,content.findAll(text=True)))
            ans.append(content)
        except:
            print head+'id'+id+' failed'
    g=open('download.txt','w')
    g.write('\n'.join(ans))
    g.close()
        
        
def test():
    fetch(head='http://proquest.safaribooksonline.com/9781449318482/')
    
if __name__=='__main__':
    test()