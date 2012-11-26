'''gaoyunzhi@gmail.com
12:50 PM 11/19/2012
'''
#coding: utf-8
#!/usr/bin/python26
from getWebpage import getWebpage
try:
    from BeautifulSoup import BeautifulSoup,SoupStrainer
except:
    from bs4 import BeautifulSoup,SoupStrainer # beta version of bs
import re,os
import codecs

header='http://zhidao.baidu.com/browse/'
SEPARATOR=[u'　',u'，',u'。',u',',u'？',u'、',u'！']
EndSign=[u'发邮箱',u'邮箱',u'全文',u'全本',u'TXT']
BeginSign=[u'木有',u'没有']
ishareHeader='http://ishare.iask.sina.com.cn/search.php?key='
googleHeader='https://www.google.com/#q='
questionHeader='http://zhidao.baidu.com/question/'

import platform,sys
if platform.uname()[1][-15:-9]=='equity':
    activate_this = '/mnt/nfs0/gyz/venv/base/bin/activate_this.py'
    execfile(activate_this, dict(__file__=activate_this))

def clean(x):
    x=x.strip()
    x=x.rstrip('/')
    return x

def clean_sentence(x):
    return x
    for a in x:#.decode('gb2312','ignore'):
        print a
    
def no_space(x):
    ans=[]
    for a in x:
        if re.match('\s',a):
            continue
        if a=='\n': continue
        #print '[',a, ord(a),']',
        ans.append(a)
    return ''.join(ans)

def separate(x):
    ans=[]
    tmp=[]
    for a in x+' ':
        if re.match('\s',a) or a in SEPARATOR:
            if tmp==[]: continue
            ans.append(''.join(tmp))
            tmp=[]
            continue
        tmp.append(a)        
    return ans

def printlist(x):
    count=0
    print '[',
    for a in x:
        if count==0:
            print a,
        else:
            print ';',a,
        count+=1
    print ']'

def grabQuestions(link=None,category_number=None,pn=0,reLoad=True):
    questions_to_return=[]
    if link==None and category_number==None:
        raise Exception('no input')
    if category_number!=None:
        newLink=header+clean(str(category_number))
        if pn!=0: newLink+='?pn='+str(pn)
    if link!=None and category_number!=None and newLink!=link:
        raise Exception('conflict input')
    if link==None: link=newLink
    page=getWebpage(link,reLoad=reLoad,dataDir='webpages')
    page=page.decode('gb2312','ignore')
    soup=BeautifulSoup(page,from_encoding="gb2312")
    questions=soup.findAll('tr',{'class':"qlist-tr"})
    for question in questions:
        number=question.find('td',{'class':'quick-num'})
        number_ans=int(str(number.contents[0]))
        question=question.find('td',{'class':'align-l'})
        cid=question['cid']
        qid=question['qid']
        qdesc=question['qdesc']
        qtitle=question['qtitle']
        if not cid.isdigit():
            print 'cid is not digit'
            print cid,qid,qdesc,qtitle
            continue
        else:
            cid=int(cid)
        if not qid.isdigit():
            print 'qid is not digit'
            print cid,qid,qdesc,qtitle
            continue
        else:
            qid=int(qid)
        qdesc=clean_sentence(qdesc)    
        qtitle=clean_sentence(qtitle)
        #if qid!=499587072: continue
        
        content=qtitle+'\n'+qdesc
        content_no_space=no_space(content)
        email=re.search('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]+',content_no_space)
        if email!=None:
            email=email.group(0)+'qq.com'
        if email!=None:
            email=re.search('\w+@\w+\.(com|cn)',content_no_space)
            if email!=None:
                email=email.group(0)
        if email==None:
            email=''
        s=u'《'+'.*'+u'》'
        s2='<<.*>>'
##        s=s.encode('gb2312','ignore')
##        print s
        title_separate=separate(qtitle)
        book_name=re.search(s, content_no_space)
        if book_name!=None:
            book_name=book_name.group(0)[1:-1]
        if book_name==None:
            book_name=re.search(s2, content_no_space)
            if book_name!=None:
                book_name=book_name.group(0)[2:-2]
            else:
                for i in xrange(len(title_separate)):
                    x=title_separate[i]
                    if u'求' in x:
                        ind=x.find(u'求')
                        if len(x)-ind>=3:
                            book_name=x[ind+1:]
                        elif i+1<len(title_separate):
                            book_name=title_separate[i+1]
                        break
                    if u'有' in x:
                        ind=x.find(u'有')
                        if len(x)-ind>=3:
                            book_name=x[ind+1:]
                        elif i+1<len(title_separate):
                            book_name=title_separate[i+1]
                        break
                    if 'txt' in x:
                        ind=x.find('txt')
                        if ind>3:
                            book_name=x[:ind]
                            break
                    if 'TXT' in x:
                        ind=x.find('TXT')
                        if ind>3:
                            book_name=x[:ind]
                            break
                        

        for x in EndSign:
            if book_name==None: break
            if x in book_name:
                ind=book_name.find(x)
                book_name=book_name[:ind]

        for x in BeginSign:
            if book_name==None: break
            if x in book_name:
                ind=book_name.find(x)
                book_name=book_name[ind+len(x):]

        if book_name!=None and '@' in book_name:book_name=None
        if book_name==None or book_name=='':
            book_name=title_separate[0]

        
        
            
        
        #print qid,int(number_ans),'[',qdesc,',',qtitle,']',email
        #printlist(title_separate)
        #print book_name
        #print '-'*30
        google_query=book_name
        if google_query in title_separate[0]:
            google_query=title_separate[0]
        questions_to_return.append((qid,int(number_ans),email,book_name,google_query,content_no_space))
        
    return questions_to_return
    
def genLink(link='',name='link'):
    return '<a href="'+link+'" target="_blank">'+name+'</a>'

def genEmail(email=None,name='email'):
    if email!=None and email!='':
        return '<a href="mailto:'+email+'" target="_blank">'+name+'</a>'
    else:
        return 'email'

def htmlTable(*args):
    ans=['<tr>']
    for arg in args:
        ans.append('<td>'+arg+'</td>')
    ans.append('</tr>')
    return '<table>'+'\n'.join(ans)+'</table>'+'<hr>'#+'<tr>'+'<td> </td>'*len(args)+'</tr>'

def to_str(x):
    if x==None: return ''
    if isinstance(x,int):
        return str(x)
    else:
        return x

def writeQuestions(des='questions.html',save_disc='all_question.txt', questions=[] ):
    if  not os.path.exists(save_disc):
        f=open(save_disc,'w')
        f.close()
    f=codecs.open(save_disc,'a',"gb2312")
    for ques in questions:
        f.write('\t'.join(map(to_str,ques))+'\n')
    f.close()
    g=open(des,'w')
    #g.write('<table>')
    g.close()
    for ques in questions:
        qid,number_ans,email,book_name, google_query, contents=ques[:6]
        if number_ans>=1: continue
        #if email==None or email=='': continue
        if book_name==None or book_name=='': continue
        g=codecs.open(des,'a',"gb2312")
        question=genLink(link=questionHeader+str(qid)+'.html',name=book_name)
        address=genEmail(email=email,name='email')
        iask=genLink(link=ishareHeader+book_name,name='ishare')
        google=genLink(link=googleHeader+google_query,name='google')
        m=len(book_name)
        #print m, 30-m, contents[:30-m]
        g.write(htmlTable(address,iask,google,question,contents[:60-m]))
        g.close()
    g=open(des,'a')
    #g.write('</table>')
    g.close()
        
def test():
    link='http://zhidao.baidu.com/browse/218'
    category_number=218
    ans=grabQuestions(category_number=218,pn=10)
##    for x in ans:
##        printlist(x)
    writeQuestions(questions=ans)

    
if __name__=='__main__':
    test()
