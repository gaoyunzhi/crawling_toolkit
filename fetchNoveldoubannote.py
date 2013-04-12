#coding: utf-8
'''
fetch novel from website
'''

from getSoup import getSoup
import re,sys

def clean(s):
    if '{' in s:
        p=s.find('{')
        q=s.find('}')
        if p<q and q-p<20:
            s=s[:p]+s[q+1:]
    if '【' in s:
        p=s.find('【')
        q=s.find('】')
        if p<q and q-p<40:
            s=s[:p]+s[q+1:]        
    return s.strip()
    
def fetch(head):
    soup=getSoup(head)
    t=soup.find('h1')
    title=t.find(text=True)
    print title
    ans=[]
    for i in xrange(0,10000,10):
        link=head+'?start='+str(i)
        soup=getSoup(link)
        notes=[]
        for x in soup.findAll('span',{'class':'rec'}):
            if not x.has_key('id') : continue
            if  x['id'][:5]!='Note-': continue
            notes.append(x['id'][5:])
        if notes==[]: break
        for note in notes:
            soup=getSoup('http://www.douban.com/note/'+note)
            note_title=soup.find('title').find(text=True)
            article=soup.find('div',{'class':"note", 'id':"link-report"})
            content=note_title+'\n'.join(map(clean,article.findAll(text=True)))+'\n\n'
            ans.append(content)
 
    g=open(title+'.txt','w')
    g.write('\n'.join(ans))
    g.close()
        
        
for x in sys.argv[1:]+['http://www.douban.com/people/3703176/notes']:
    if not x: continue
    fetch(head=x)
    
