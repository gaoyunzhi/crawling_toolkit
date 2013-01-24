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
    res=c.execute("SELECT * FROM `location` WHERE `latitude` IS NOT NULL AND `longitude` IS NOT NULL")
    n=res
    print n
    cities=c.fetchall()
    for city in cities:
        if city["complete_descrip"].strip()!="": continue      
        name=city["location_name"]
        page=getWebpage('http://wikitravel.org/en/'+name)
        soup=BeautifulSoup(page)
        paras=[]
        for x in soup.findAll('p'):        
            paras.append(''.join(map(clean_t,x.findAll(text=True))))
            paras=map(clean,paras)
        paras=[x for x in paras if x!='']
        paras.append('</a href="'+'http://wikitravel.org/en/'+name+'">From wiki travel<a>')
        article='\n'.join(paras)
        article=article.decode('ascii','ignore') 
        article=MySQLdb.escape_string(article)
        id=city["location_id"]
        write_to_sql_item(id,article)
        
        
        


                      
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
    c.execute(
              "UPDATE `location` SET `complete_descrip` = '"+article+
              "' WHERE `location_id` = "+str(num)
            )

            

open_sql()
ans=fetch()

