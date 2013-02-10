from getWebpage import getWebpage
from extractLinks import extractLinks
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import MySQLdb
import sqlite3
from math import sqrt
from random import sample
N=1000
def clean(s):
    s=s.replace(' '*2,' ')
    return s.strip()
def clean_t(s):
    if '[' in s:
        p=s.find('[')
        q=s.find(']')
        if p<q and q-p<40:
            s=s[:p]+s[q+2:]        
    return s

def get_reg_id(lst):
    if lst==["E"]: return 1
    if lst==["S"]: return 2
    if lst==["W"]: return 3
    if lst==["I"]: return 4
    if lst==sorted(["E","S"]): return 5
    if lst==sorted(["E","W"]): return 6
    if lst==sorted(["E","I"]): return 7
    if lst==sorted(["S","W"]): return 8
    if lst==sorted(["I","S"]): return 9
    if lst==sorted(["I","W"]): return 10
    if lst==sorted(["E","S","W"]): return 11
    if lst==sorted(["S","E",'I']): return 12
    if lst==sorted(["S","W",'I']): return 13
    if lst==sorted(["S","E",'I','W']): return 14
    print lst,"ERROR!!!"
    
def fetch(): 
    res=c.execute("SELECT * FROM `location` WHERE `latitude` IS NOT NULL AND `longitude` IS NOT NULL AND `location_id`>30" )
    n=res
    cities=c.fetchall()
    to_remove=[]
    for i in xrange(n):
        for j in xrange(i):
            if cities[i]['location_name'].strip()==cities[j]['location_name'].strip():
                to_remove.append(j)
    cities=[cities[i] for i in xrange(n) if not i in to_remove]
    for x in cities:
        x["location_name"]=x["location_name"].strip()
    n-=len(to_remove)    
    for days in xrange(2,20):
        count=1       
        for i in xrange(100000):
            cs=sample(cities,days)
            des=0
            name=''
            desc="Location visited: "
            regs=[]
            cts=[]
            for i in xrange(days-1):             
                des+=sqrt((cs[i]['latitude']-cs[i+1]['latitude'])**2+(cs[i]['longitude']-cs[i+1]['longitude'])**2)
                name+=cs[i]['location_name']+', '
                desc+=cs[i]["location_name"]+", "
                regs.append(cs[i]["region"])
                cts.append(cs[i]["location_id"])
            if des>sqrt(days)*(days-1)/3:continue
            name+=str(cs[days-1]['location_name'])+' '+str(days)+" day tour"
            id=count+10*days+7000
            desc+=cs[days-1]["location_name"]+\
                    ". Distance of travel: around "+str(des)+" miles."
            go=0
            regs=list(set(regs+[cs[days-1]["region"]]))
            regs.sort()
            regs_id=get_reg_id(regs)
            cts.append(cs[days-1]["location_id"])
            write_to_sql_item(id=id,go=go,region=regs_id,name=name,
                              cities=cts,
                              desc=desc,days=days,hp=1)
            count+=1
            if count>=10: break

def open_sql():
    global c
    dbhost="sql.mit.edu"
    dbname= "liyihua+apparate"
    dbusername="liyihua"
    dbpassword="3217132"
    connection = MySQLdb.connect (host = dbhost, 
                              user = dbusername, 
                              passwd = dbpassword, 
                              db = dbname)
    c=connection.cursor(MySQLdb.cursors.DictCursor)
    
def write_to_sql_item(id=0,go=2,region=0,name='',cities=[],desc="",days=0,hp=0):   
    day0="INSERT INTO itinerary (id,length,title,description,go,region,day,city_id,hp)"+\
              " VALUES ('"+str(id)+"','"+str(days)+"', '"+\
              name+"', '"+desc+"', '"+str(go)+"', '"+str(region)+"', '"+'0'+"', '"+str(cities[-1])+"', '"+str(hp)+"')"
    print id
    c.execute(day0)
    for d in xrange(1,days+1):
        c.execute("INSERT INTO itinerary (id,day,city_id)"+
              " VALUES ('"+str(id)+"','"+str(d)+"', '"+str(cities[d-1])+"')")
        

            

open_sql()
ans=fetch()

