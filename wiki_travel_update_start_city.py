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
    res=c.execute("SELECT * FROM `itinerary` WHERE `day`=0")
    itis=c.fetchall()
    for iti in itis:
        id=iti["id"]
        c.execute("SELECT * FROM `itinerary` WHERE `id`="+str(id)+" AND `day`="+str(1))
        row=c.fetchone()
        start_city=row["city_id"]
        write_to_sql_item(id,0,start_city)  

                      
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
    
def write_to_sql_item(num,day,city_id):  
    sql= "UPDATE `itinerary` SET `city_id` = '"+str(city_id)+\
              "' WHERE `id`="+str(num)+" AND `day`="+str(day)
    c.execute(sql)

            

open_sql()
ans=fetch()

