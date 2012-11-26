import urllib,urllib2

def login(email='bajie90@gmail.com',pd='dBajie90',\
          login_url='https://www.douban.com/accounts/login'):
    postDict = {
        'source':'index_nav',
        'form_email':email,
        'form_password':pd,
        'remember':'on',
        'Request':'POST /accounts/login HTTP/1.1',
        'Accept':'text/html, application/xhtml+xml, */*',
        'Referer':'http://www.douban.com/',
        'Accept-Language':'en-US',
        'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept-Encoding':'gzip, deflate',
        'Host':'www.douban.com',
        'Content-Length':'80',
        'Connection':'Keep-Alive'
        }
    postData = urllib.urlencode(postDict)
    req = urllib2.Request(login_url, postData)
    resp = urllib2.urlopen(req)
    f=open('tmp.html','w')
    f.write(resp.read())
    f.close()

#login()

cookies='''ck="3bMe"; __utmc=30149280; bid="cwoRAvJOWdQ"; dbcl2="4898454:5qnPL5l4FFw"; __utma=30149280.127203582.1353697363.1353697363.1353697363.1; __utmb=30149280.4.10.1353697363; __utmz=30149280.1353697363.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.489'''
page_info = urllib2.build_opener()
page_info.addheaders = [('User1', 'safari/536.25')]
page_info.addheaders.append(('Cookie', cookies))
postDict={}
link='http://www.douban.com/people/gyz/'
postData='ck=3bMe&bp_text=test2&bp_submit=+%E7%95%99%E8%A8%80+'
req = urllib2.Request(link, postData);
page = page_info.open(req)
f=open('tmp1.html','w')
f.write(page.read())
f.close()


    
