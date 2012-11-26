'''
gaoyunzhi@gmail.com
8:38 AM 10/16/2012
getTraffic: get traffic of wikipedia page 
input: title, date=yyyymm
output: visited number in that month

'''
from getWebpage import getWebpage
import json
import json

def getTraffic(title, date , silent=True,country='en'):
    date=str(date)
    link='http://stats.grok.se/json/'+country+'/' + date +'/'+title
    if silent==False: print link
    page=getWebpage(link)
    jsondata= json.loads(page)
    daily_views =jsondata['daily_views']
    tot = 0
    days = 0
    for day, views in daily_views.iteritems():
        tot+=views
        days+=1
    return tot*1.0/days

def test():
    title='14th_Street_%E2%80%93_Union_Square_(New_York_City_Subway)'
    date=201209
    print getTraffic(title, date)

if __name__=='__main__':
    print 'getTraffic gets traffic of wikipedia page'
    print 'input: title, date=yyyymm'
    print 'output: visited number in that month'
    print 'some test'
    test()
