'''gaoyunzhi@gmail.com
12:56 PM 10/15/2012
get the local fname of a webpage
currently saveing as the same as the last piece of the address, without extension
input: webpage link
output: local fname
'''
def toASN(s):
    ans=[]
    for x in s:
        if ord(x)<128:
            ans.append(x)
    return ''.join(ans)

def toFname(link,hasHtml=True):
    link=toASN(link)
    link=link.strip()
    dotInd=link.rfind('.')
    if dotInd!=-1 and dotInd+10>len(link):
        link=link[:dotInd]
    while link[-1]=='/': link=link[:-1]
    if link=='': 
        print link+' is not a valid web address'
        return None
    name=link.split('/')[-1]
    name=toASN(name)
    name=str(name)
    name=name.translate(None,' / ? < > \ : * | "')
    if len(name)>100:
        name=name.decode('utf8')[:100]
    hashc=hash(link) %1000
    link=name+'_'+str(hashc)
    if hasHtml==True:
        return link+'.html'
    else:
        return link

def test():
    print toFname('http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvlimit=1&format=xml&titles=59th_Street_%E2%80%93_Columbus_Circle_(IRT_Broadway_%E2%80%93_Seventh_Avenue_Line)&rvstart=20100101')
    print toFname('http://en.wikibooks.org/wiki/Python_Programming/Strings')
    print toFname('Strings')
    print toFname('http://en.wikibooks.org/wiki/Python_Programming/Strings')

if __name__=='__main__':
    print 'this is a file contains Tofname, which get the local fname of a webpage'
    print 'running test'
    test()
