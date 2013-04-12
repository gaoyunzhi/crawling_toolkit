from getSoup import getSoup
import re

ans=[]

def format(x):
    x=x.split()
    if len(x)!=2: return False
    if not x[-1].isdigit(): return False
    if x[0] in ['Jan','Feb','Mar','Apr','May',
                'Jun','July','Aug','Sep','Oct',
                'Nov','Dec']:
        return True
    return False
  
def date_try1(x): 
    x=x.split(',')
    if len(x)!=2: return False
    x[0]=x[0].strip()
    x[1]=x[1].strip()
    if format(x[0]) and format(x[1]):
        return x[0],x[1]
    return False 

def date_try2(x): 
    x=x.split('and')
    if len(x)!=2: return False
    x[0]=x[0].strip()
    x[1]=x[1].strip()
    if format(x[0]) and format(x[1]):
        return x[0],x[1]
    return False 

def date_try3(x): 
    x=x.split('and')
    if len(x)!=2: return False
    x[0]=x[0].strip()
    x[1]=x[1].strip()
    if format(x[0]) and x[1].isdigit():
        return x[0],x[0].split()[0]+' '+x[1]
    return False 
    
def date2(x):
    lind=x.find('[')
    rind=x.find(']')
    if lind==-1 or rind==-1: 
        lind=x.find('(')
        rind=x.find(')')
    if lind==-1 or rind==-1:
        return False
    x=x[lind+1:rind]
    if date_try1(x):
        return date_try1(x)
    if date_try2(x):
        return date_try2(x) 
    if date_try3(x):
        return date_try3(x)    
    
    

def date(x):
    if len(x)<3: return False
    if x[0]!='[': return False
    if x[-1]!=']': return False
    x=x[1:-1]
    return format(x)

def data2(s):
    points1=s[23:26]
    points2=s[27:30]
    if len(points1)!=3: return False
    if len(points2)!=3: return False
    if points1[0].isdigit() and points1[2].isdigit() and points1[1]=='-' and \
        points2[0].isdigit() and points2[2].isdigit() and points2[1]=='-':
        t1=s[:23].strip()
        t2=s[30:].strip()
        if '  ' in t1 or '  ' in t2 or '\t' in t1 or '\t' in t2:
            return False
        if (not t1[0].isupper()) or (not t2[0].isupper()):
            return False
        p1=int(points1[0])
        p2=int(points1[2])
        p3=int(points2[0])
        p4=int(points2[2])
        return t1,t2,p1,p2,p3,p4       
    return False

def data3(s):
    points1=s[61:64]
    points2=s[66:69]
    if len(points1)!=3: return False
    if len(points2)!=3: return False
    if points1[0].isdigit() and points1[2].isdigit() and points1[1]=='-' and \
        points2[0].isdigit() and points2[2].isdigit() and points2[1]=='-':
        t1=s[:25].strip()
        t2=s[30:55].strip()
        if '  ' in t1 or '  ' in t2 or '\t' in t1 or '\t' in t2:
            return False
        if (not t1[0].isupper()) or (not t2[0].isupper()):
            return False
        p1=int(points1[0])
        p2=int(points1[2])
        p3=int(points2[0])
        p4=int(points2[2])
        return t1,t2,p1,p2,p3,p4       
    return False

    
def data(s):
    points=s[14:17]
    if len(points)!=3: return False
    if points[0].isdigit() and points[2].isdigit() and points[1]=='-':
        t1=s[:14].strip()
        t2=s[17:].strip()
        if '  ' in t1 or '  ' in t2 or '\t' in t1 or '\t' in t2:
            return False
        if (not t1[0].isupper()) or (not t2[0].isupper()):
            return False
        p1=int(points[0])
        p2=int(points[2])
        return t1,t2,p1,p2        
    return False

def addDom(link,loc,year):
    soup=getSoup(link)    
    for x in soup.findAll('pre'):
        time=None
        time1=None
        time2=None
        x=str(x).split('\n')
        for y in x:
            y=y.strip()
            if date(y):
                time=y[1:-1]
            elif data(y):
                t1,t2,p1,p2=data(y)
                ans.append([t1,p1-p2,year,time,t2,loc,'home','domestic'])
                ans.append([t2,p2-p1,year,time,t1,loc,'away','domestic'])                
            if date2(y):
                time1,time2=date2(y)
            elif data2(y):
                t1,t2,p1,p2,p3,p4=data2(y)
                ans.append([t1,p1-p2,year,time1,t2,loc,'home','domestic'])
                ans.append([t2,p2-p1,year,time1,t1,loc,'away','domestic'])
                ans.append([t1,p3-p4,year,time2,t2,loc,'home','domestic'])
                ans.append([t2,p4-p3,year,time2,t1,loc,'away','domestic'])
                


domPage=getSoup('http://www.rsssf.com/resultsp00.html')
for loc in ['England','Italy','Spain']:
    for x in domPage.findAll('a'):
        text=x.find(text=True)
        text=text.split()
        if len(text)!=2: continue
        if text[0]!=loc: continue
        link='http://www.rsssf.com/'+x['href']
        addDom(link,loc,text[1])
        
      
def addInt(link,year):
    soup=getSoup(link) 
    for x in soup.findAll('pre'):
        time1=None
        time2=None
        x=str(x).split('\n')
        for y in x:
            y=y.strip()              
            if date2(y):
                time1,time2=date2(y)
            elif data3(y):
                t1,t2,p1,p2,p3,p4=data3(y)
                ans.append([t1,p1-p2,year,time1,t2,'international','home','international'])
                ans.append([t2,p2-p1,year,time1,t1,'international','away','international'])
                ans.append([t1,p3-p4,year,time2,t2,'international','home','international'])
                ans.append([t2,p4-p3,year,time2,t1,'international','away','international'])
     
     

intPage=getSoup('http://www.rsssf.com/ec/ecomp.html')
for year in intPage.findAll('a'):
    y=str(year.find(text=True))
    if y.startswith('20'):
        link='http://www.rsssf.com/ec/'+year['href']
        addInt(link,y)
print len(ans)
f=open('ans.txt','w')
for x in ans:
    x[0]=x[0].replace(' ','')
    x[4]=x[4].replace(' ','')
    x[2]=x[2].replace('-','/')
    f.write('\t'.join(map(str,x))+'\n')
f.close()
