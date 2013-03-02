'''
parse qq friendlist to gmail
'''
f=open('C:\Dropbox\current\important\qq_friend.txt')
g=open('infos_qq.csv','w')
N=9 # seems to be the length of qq number, have no knowledge of qq
qqs=set()
g.write('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Group Membership,E-mail 1 - Type,E-mail 1 - Value,E-mail 2 - Type,E-mail 2 - Value,Phone 1 - Type,Phone 1 - Value'+'\n')
for line in f:
    line=line.decode('gbk').strip()
    if not line: continue
    atInd=line.rfind('@')
    qq=line[atInd-9:atInd+7]
    print line,qq
    qq_num=int(qq[:9])
    if qq_num in qqs: continue
    qqs.add(qq_num)
    name=line[atInd+8:]
    if not name: name=line[:atInd-9]
    g.write(name)
    g.write(','+name)
    g.write(',,,,,,,,,,,,,,,,,,,,,,,,'+',,,'+qq+',,'+''+',,'+''+'\n')
g.close()
    
    