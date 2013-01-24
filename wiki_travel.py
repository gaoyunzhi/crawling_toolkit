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
def fetch(head):    
    headP=getWebpage(head)
    ind=head.rfind('/')
    domain=head[:ind+1]
    main_loc=head[ind+1:]
    count=0
    locs={main_loc:'United States of America'}
    aganda=[main_loc]
    p=0
    while p<len(aganda) and count<N:
        loc=aganda[p]
        p+=1
        links=extractLinks(link=domain+loc,requireLinkStart='/en/',
                     requiredKeys=['href','title'],
                     containedIn=('ul',{})
                     )
        links=[x for x in links if not ']' in x['title']]
        links=[x for x in links if not ':' in x['title']]
        for l in links:
            loc=l['href'][4:]
            if loc in locs: continue 
            aganda.append(loc)
            locs[loc]=l['title']
            count+=1
            if count%100==0: print count
    f=open('locs.txt','w')
    for loc in aganda:
        f.write(loc+'\n')
    f.close()
    
    ans=[]
    for num in xrange(len(aganda)):
        loc=aganda[num]               
        title=locs[loc]
        c.execute("SELECT * FROM `location` WHERE `location_name`='"+
              MySQLdb.escape_string(title)+"'  LIMIT 1")
        if c.fetchone()!=None: continue
        c.execute("SELECT * FROM `location` WHERE `location_id`='"+
              MySQLdb.escape_string(str(num+10**7))+"'  LIMIT 1")
        if c.fetchone()!=None:
            print 'id'+str(num)+' duplicated'
            continue
        try: 
            page=getWebpage(domain+loc)
            soup=BeautifulSoup(page)
        except:
            continue        
        paras=[]
        for x in soup.findAll('p'):
            paras.append(''.join(map(clean_t,x.findAll(text=True))))
        paras=map(clean,paras)
        paras=[x for x in paras if x!='']
        article='\n'.join(paras)
        title=title.decode('ascii','ignore')
        article=article.decode('ascii','ignore')
        ans.append([title,article]) 
        article=MySQLdb.escape_string(article)
        title=MySQLdb.escape_string(title)  
        write_to_sql_item(num,title,article)
    return ans
                      
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
    c=connection.cursor()
    
def write_to_sql_item(num,title,article):    
    c.execute("INSERT INTO location (location_id, location_name, complete_descrip)"+
              " VALUES ('"+str(num+10**7)+"','"+title+"', '"+
              article+"')")

            

open_sql()
ans=fetch(head='http://wikitravel.org/en/United_States_of_America')

