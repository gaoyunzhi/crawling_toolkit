from getWebpage import getWebpage
from extractLinks import extractLinks
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import MySQLdb
import sqlite3
from googlemaps import GoogleMaps
gmaps = GoogleMaps('api_key')



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
    cities=c.fetchall()
    for city in cities:     
        name=city["location_name"]
        id=city["location_id"]
        if name.strip()=="": continue
        if city['latitude'] and city['longitude']: continue
        
        address = city["location_name"]+", UK"
        lat, lng = gmaps.address_to_latlng(address)
        if 40<lat<60 and -10<lng<10:
            write_to_sql_item(id,lat,lng)
        else:
            print id,name,lat,lng
        
        
        


                      
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
    
def write_to_sql_item(num,lat,lng):    
    c.execute(
              "UPDATE `location` SET `latitude` = "+str(lat)+", `longitude`="+str(lng)+
              " WHERE `location_id` = "+str(num)
            )

            

open_sql()
ans=fetch()

