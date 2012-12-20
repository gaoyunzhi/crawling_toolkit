'''gaoyunzhi@gmail.com
1:09 PM 10/15/2012
get saved webpage, if not saved, save the webpage before doing this
input: webpage link
output: webpage as string
mutation: if the webpage is not saved, save it
'''
from sysPath import createPath,combinePath
import urllib2,os,time,sys
from toFname import toFname

def getWebpage(link='', dataDir='webpages', timeSleep=0, 
               cookies='', reLoad=False, debug=False, read=True,referer='',info=''):
    link=link.strip()
    if link=='': return
    createPath(dataDir)
    fname=combinePath(dataDir,toFname(cookies+link+info))
    if not reLoad:
        try:
            f=open(fname,'r')
            page=f.read()
            f.close()
            if debug: print 'read from cached file'
            return page
        except:
            pass
    
    if debug: print 'reading from web' 
    time.sleep(timeSleep)       
    for i in range(10):
        try:
            page_info = urllib2.build_opener()
            page_info.addheaders = [('User1', 'safari/536.25'),
                                    ('Cookie', cookies),
                                    ('Referer',referer)
                                    ]
            page = page_info.open(link)
            if read: 
                try:
                    page=page.read()
                except:
                    print 'error reading page, try again (until trying time reach 10)'
                    print link
                    continue
            break
        except (urllib2.HTTPError,urllib2.URLError), e:
            print e.code,
            page=''
        time.sleep(timeSleep)
    if not read: return
    if page=='':
        print 'failed getWebpage', link 
        return
    if os.path.exists(fname):
        fileMTime=os.path.getmtime(fname)
        newFileName=fname[:-5]+'_'+str(fileMTime)+'.html'
        os.renames(fname, newFileName)
    f=open(fname,'w')
    f.write(page)
    f.close()
    return page

def test():
    cookies=''
    getWebpage(cookies=cookies, #reLoad=True,
               link='https://webim.feixin.10086.cn/main.aspx',
               debug=True)


if __name__=='__main__':
    print 'contains getWegpage method'
    print 'get saved webpage, if not saved, save the webpage before doing this'
    print 'some tests'
    test()
    
