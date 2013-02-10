from getWebpage import getWebpage
from extractLinks import extractLinks
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import MySQLdb
import sqlite3
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
def fetch():
    res=c.execute("SELECT * FROM `location`")
    n=res
    print n
    cities=c.fetchall()
    for city in cities:
        if city["short_descrip"].strip()!="": continue      
        article=city["complete_descrip"]
        id=city["location_id"]
        ind=article[100:].find('.')
        sd=article[:100+ind+1]
        write_to_sql_item(id,MySQLdb.escape_string(sd))

                      
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
    
def write_to_sql_item(num,article):   
    sql= "UPDATE `location` SET `short_descrip` = '"+article+\
              "' WHERE `location_id` = "+str(num)
    c.execute(sql)

            

open_sql()
ans=fetch()

