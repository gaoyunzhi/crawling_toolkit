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
    res=c.execute("SELECT * FROM `itinerary` WHERE `day`=0 AND `hp` IS NULL")
    n=res
    itis=c.fetchall()    
    for iti in itis:
        id=iti['id']
        print id
        c.execute("UPDATE `itinerary` SET `hp`=0 WHERE `id`="+str(id)+" AND `day`=0")
    
    
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
        

            

open_sql()
ans=fetch()

