link='http://read.360buy.com/14532/'
    chapters=extractLinks(link=link, requireLinkStart=link,avoidKeys=['img','alt','src'],requireLinkEnd='.html')
    print chapters
    content=getWebpage(link)
    soup=BeautifulSoup(content)
    paras=soup.findAll('div',{'class':'paragraph'})
    intro=soup.find('div',{'class':'bookintro'})
    book_name=soup.find('div',{'id':'book-cover'}).find('a')['title']
    print 'collecting: ',book_name
    f=open(book_name+'.txt','w')
    f.write('intro: ')
    for y in intro.findAll(text=True):
        if y.encode('utf8','ignore').strip()=='': continue
        f.write(y.encode('utf8','ignore')+'\n')
    for x in paras:
        for y in x.findAll(text=True):
            f.write(y.encode('utf8','ignore')+'\n')
    f.close()
    start=int(chapters[0]['href'][len(link):-5])
    end=int(chapters[-1]['href'][len(link):-5])+20
    chapterD={}
    for x in chapters:
        num=int(x['href'][len(link):-5])
        title=x['title']
        chapterD[num]=title
    count=0
    for i in range(start,end):
        chapter=link+str(i)+'.html'
        content=getWebpage(chapter)
        soup=BeautifulSoup(content)
        content=soup.find('div',{'id':'zoom'}) 
        f=open(book_name+'.txt','a')
        if i in chapterD:
            f.write('\n\n'+chapterD[i].encode('utf8','ignore')+'\n')
        if content==None: continue
        for y in content.findAll(text=True):
            if y.encode('utf8','ignore').strip()=='': continue
            f.write(y.encode('utf8','ignore')+'\n')
        f.close()
        #if count>5:break
        count+=1