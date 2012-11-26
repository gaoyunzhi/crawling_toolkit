'''gaoyunzhi@gmail.com
5:40 PM 10/14/2012
extract all links in one webpage
input: webpage link
output: link fields
mutation: if the webpage is not saved, save it
for the convience of the current use, sacrificed generality 
'''
#coding: utf-8
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
from getWebpage import getWebpage # get the local fname of a webpage

def extractLinks(link='', requireLinkStart='', requiredKeys=[],\
                 specification=[], containedIn=None,numTable_level_1=None,\
                 numTable_level_2=None, avoidKeys=[],coo='',requireLinkEnd=''):
    ans=[]
    content=getWebpage(link, cookies=coo)     
    soup = BeautifulSoup(content)
    if containedIn!=None:
        tables=soup.findAll(containedIn[0],containedIn[1])
    else:
        tables=[soup]
    for table in tables[:numTable_level_1]:
        for field in table.findAll('a')[:numTable_level_2]:
            if field.has_key('href'): 
                extLink=field['href']
                satisfySpec=True
                for subfield, require in specification:
                    if not field.has_key(subfield):
                        satisfySpec=False
                        break
                    if not require in field[subfield]:
                        satisfySpec=False
                        break
                for requiredKey in requiredKeys:
                    if not field.has_key(requiredKey):
                        satisfySpec=False
                        break
                for avoidKey in avoidKeys:
                    if isinstance(avoidKey,str):
                        if field.has_key(avoidKey):
                            satisfySpec=False
                            break
                    else:
                        akey,akeyValue=avoidKey
                        if field.has_key(akey) and field[akey]==[akeyValue]:
                            satisfySpec=False
                            break
                if satisfySpec==False: continue 
                if extLink[:len(requireLinkStart)]==requireLinkStart and \
                   (requireLinkEnd=='' or extLink[-len(requireLinkEnd):]==requireLinkEnd):
                    ans.append(field)
    return ans
    

def test():
    link='http://read.360buy.com/14532/'
    chapters=extractLinks(link=link, requireLinkStart=link,avoidKeys=['img','alt','src'],requireLinkEnd='.html')
    print chapters
    content=getWebpage(link)
    soup=BeautifulSoup(content)
    paras=soup.findAll('div',{'class':'paragraph'})
    intro=soup.find('div',{'class':'bookintro'})
    book_name=soup.find('div',{'id':'book-cover'}).find('a')['title']
    print 'collecting: ',book_name
    f=open(book_name+'.txt','w')
    f.write('intro: ')
    for y in intro.findAll(text=True):
        if y.encode('utf8','ignore').strip()=='': continue
        f.write(y.encode('utf8','ignore')+'\n')
    for x in paras:
        for y in x.findAll(text=True):
            f.write(y.encode('utf8','ignore')+'\n')
    f.close()
    start=int(chapters[0]['href'][len(link):-5])
    end=int(chapters[-1]['href'][len(link):-5])+20
    chapterD={}
    for x in chapters:
        num=int(x['href'][len(link):-5])
        title=x['title']
        chapterD[num]=title
    count=0
    for i in range(start,end):
        chapter=link+str(i)+'.html'
        content=getWebpage(chapter)
        soup=BeautifulSoup(content)
        content=soup.find('div',{'id':'zoom'}) 
        f=open(book_name+'.txt','a')
        if i in chapterD:
            f.write('\n\n'+chapterD[i].encode('utf8','ignore')+'\n')
        if content==None: continue
        for y in content.findAll(text=True):
            if y.encode('utf8','ignore').strip()=='': continue
            f.write(y.encode('utf8','ignore')+'\n')
        f.close()
        #if count>5:break
        count+=1
        
    

    
if __name__=='__main__':
    print '''extract all links in one webpage
        input: webpage link
        output: link fields
        mutation: if the webpage is not saved, save it
        for the convience of the current use, sacrificed generality '''
    print 'some test'
    test()
