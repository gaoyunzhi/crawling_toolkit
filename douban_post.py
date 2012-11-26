import urllib,urllib2,codecs,urlparse
# -*- coding:utf8 -*-
def post(text):
    cookies='''ck="3bMe"; __utmc=30149280; bid="cwoRAvJOWdQ"; dbcl2="4898454:5qnPL5l4FFw"; __utma=30149280.127203582.1353697363.1353697363.1353697363.1; __utmb=30149280.4.10.1353697363; __utmz=30149280.1353697363.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.489'''
    page_info = urllib2.build_opener()
    page_info.addheaders.append(('Cookie', cookies))
    postDict={}
    link='http://www.douban.com/people/gyz/'
    postData='ck=3bMe&bp_text='+text+'&bp_submit=+%E7%95%99%E8%A8%80+'
    req = urllib2.Request(link, postData);
    page_info.open(req)


f=codecs.open(u'(英汉)《英汉对照唐诗三百首》.txt','r','gbk')
poems=f.read().splitlines()
f.close()
to_post=''
count=0
for line in poems:
    if line[:10]!='-'*10:
        to_post+=line+' '
    else:
        if to_post.strip()=='':
            to_post=''
            continue
        count+=1        
        #print urllib.quote(to_post.encode('utf-8'))
        if count>70: post(urllib.quote(to_post.encode('utf-8')))
        to_post=''

     
print urllib.quote('唐诗三百首')
#post(urllib.quote('唐诗三百首'))
