'''
gaoyunzhi@gmail.com
11:49 AM 10/16/2012
genTable from link field
input: file containing all link fields
output: tab sperated data
'''
#!/usr/bin/python26
import platform
if platform.uname()[1][-15:-9]=='equity':
    activate_this = '/mnt/nfs0/gyz/venv/base/bin/activate_this.py'
    execfile(activate_this, dict(__file__=activate_this))
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
from sysPath import sysPath
from getRevId import getRevId
from propertyLookUp import numImage, contentLen
from getTraffic import getTraffic
import datetime
from getWebpage import getWebpage
import os


def genTable(filename='../../testData/testingMonuments.txt',\
             outfname='../../testData/testingMonumentsData_week4_all.csv', \
             months=None,yearBegin=2009, yearEnd=2015,silent=True,endLine=None,\
             testNow=False, country='en'):
    now = datetime.datetime.now()
    now=(int(now.year),int(now.month))
    if months==None:
        months=[]
        for year in range(yearBegin,yearEnd):
                for month in range(1,13):
                    if (year, month)>=now: break
                    months.append(str(year)+'0'*(2-len(str(month)))+str(month))
    months=map(str,months)
    filename=sysPath(filename)
    f=open(filename,'r')
    links=f.read().splitlines()
    f.close()    
    #soup=BeautifulSoup(links)
    titleLine=['linkTitle']
    for month in months:
        titleLine.append('Img'+month)
        titleLine.append('Content'+month)
        titleLine.append('Traffic'+month)
    if not os.path.exists(outfname):
        outf=open(outfname,'w')
        outf.write('\t'.join(titleLine)+'\n')
        start=0
        outf.close()
    else:
        outf=open(outfname,'r')
        start=len(outf.read().splitlines())
        outf.close()
    count=0
##    for field in soup.findAll('a')[:endLine]:
    for linkTitle in links:
        index=linkTitle.find('/wiki/')
        if index!=-1:
            linkTitle=linkTitle[index+6:]
        count+=1
        if count<start: continue
##        if not field.has_key('title'): continue
##        linkTitle=field['href'][6:]
##        officialTitle=field['title']
        curLine=[linkTitle]
        for month in months:
            date=month+'01'
            revId=getRevId(linkTitle, date+'000000' , silent=silent,country=country) # 6 zeros for h,m,s
            if not silent: print 'revId=',revId
            if revId==None:
                curLine+=['','','']
                continue
            link='http://'+country+'.wikipedia.org/w/index.php?oldid='+revId
            if testNow: print 'title=',linkTitle, 'link=',link,'month=',month
            if not silent: print 'prepare'
            page=getWebpage(link, timeSleep=0.5,silent=silent)
            if not silent: print 'got page'
            soup=BeautifulSoup(page)
            if not silent: print 'got soup'
            numImg=numImage(soup)            
            if not silent: print 'got num'
            conLen=contentLen(soup)
            if not silent: print 'got len'
            traffic=str(getTraffic(linkTitle,month, silent=silent, country=country))
            if not silent: print 'got history'
            curLine+=[numImg, conLen, traffic]
        curLine=map(str, curLine)
        outf=open(outfname,'a')
        outf.write('\t'.join(curLine)+'\n')
        outf.close()

def test():
    #address=u'../../data/webpages/apiphpaction=query&prop=revisions&rvlimit=1&format=xml&titles=59th_Street_%E2%80%93_Columbus_Circle_(IRT_Broadway_%E2%80%93_Seventh_Avenue_Line)&rvstart=20100101(http--en.wikipedia.org-w).html'
    #f=open(address,'w')
    
    genTable(months=[200910,201010,201110,201210,201208],\
             filename='../../testData/week6_m.txt',\
             outfname='../../testData/testingMonumentsData_week6_all.csv', country='nl',\
             silent=True)

if __name__=='__main__':
    print 'genTable from link field, to do further regression'
    print 'input: file containing all link fields'
    print 'output: tab sperated data'
    print 'some tests'
    test()
                
        
        

            
            
