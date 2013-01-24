#coding: utf-8
'''
for txt comparison
'''
import os
import codecs
def clean_lines(line):
    line=line.strip()
    line=line.strip(u'　')
    return line

def clean_files(s):
    lines=s.splitlines()
    lines=map(clean_lines,lines)
    lines=[x for x in lines if x!='']
    lines='\n'.join(lines)
    lines=lines.replace(' ','')
    lines=lines.replace('】','')
    return lines

def inc(x):
    return x+1

def common(words):
    if words==[words[0]]*n: return words[0]
    for q in ['“','”']:
        if q in words:
            f=True
            for w in words:
                if not w in ['"',q]:
                    f=False
                    break
            if f: return q

def compare(folder='compare'):
    global n
    files=[]
    for file in os.listdir(folder):
        name, ext = os.path.splitext(file)
        if name=='output': continue
        f=codecs.open(os.path.join(folder,file),'r','gbk')
        files.append(f.read())
        f.close()
    n=len(files)
    p=[0]*n
    files=map(clean_files,files)  
    res=[]
    while True:
        cur=common([files[x][p[x]] for x in xrange(n)])      
        if cur:
            res.append(cur)
            p=map(inc,p)
        else:
            break
    print ''.join(res)[-30:]
    for i in xrange(n):
        print files[i][p[i]]
     


compare()
