'''gaoyunzhi@gmail.com
1:14 PM 10/15/2012
sysPath
change path according to the system
deal with windows and non-windows
input: windoes path
output: path according to the system

folderPath:
make a folderPath with ending / or \, at the same time, change according to the system.
'''
# -*- coding:utf8 -*-
import os
import platform

def combinePath(x,y):
    x=folderPath(x)
    y=sysPath(y)
    if y=='': return x
    if y[0]==systemSpliter():y=y[1:]
    return x+y

    
def createPath(path):
    path=sysPath(path)
    if path!='' and (not os.path.exists(path)):
        try:
            os.makedirs(path)
            return 'created'
        except:
            return 'failed'
    else:
        return 'alreay exist'
    
def sysPath(path):
    path=path.strip()
    if os.name=='nt' or platform.uname()[1][-15:-9]=='equity':
        path=path.replace('\ '[:1],'/ '[:1])
    else:
        path=path.replace('/ '[:1],'\ '[:1])
        
    return path



def folderPath(path):
    path=path.strip()
    if path=='': return path
    if path[-1]!='/' and path[-1]!='\ '[:-1]:
        path=path+'/'
    return sysPath(path)

def testSysPath():
    print sysPath('C:\Users\gyz\Dropbox\classes\ml\HW2\code')
    print sysPath('C:\Users\gyz\Dropbox\classes\ml\HW2\code\ '[:-1])
    print sysPath('C:/Users\gyz\Dropbox\classes\ml\HW2\code\ '[:-1])

def testFolderPath():
    print folderPath('C:\Users\gyz\Dropbox\classes\ml\HW2\code')
    print folderPath('C:\Users\gyz\Dropbox\classes\ml\HW2\code\ '[:-1])
    print folderPath('C:/Users\gyz\Dropbox\classes\ml\HW2\code\ '[:-1])

def testCreatePath():
    createPath('a/')
    createPath('b/c/')
    createPath('d/e/')
    createPath(' f\g/')

def systemSpliter():
    if os.name=='nt' or platform.uname()[1][-15:-9]=='equity':
        return '/ '[:1]
    else:
        return '\ '[:1]
    
def createFile(path,debug=False,force=False):
    path=sysPath(path)
    ind=path.rfind(systemSpliter())
    if ind!=-1: 
        floder=path[:ind]
        createPath(floder)
    name=path[ind+1:]    
    if os.path.exists(path):
        if not force: return 'already exist'
    try:
        f=open(path,'w')
        f.close()
        return 'created'
    except:
        if debug:print 'create '+ path+' failed!'
        return 'failed'
    
             
def testCreateFile():
    createFile('infos.txt')
         
if __name__=='__main__':
    pass 
    testCreateFile()
    '''
    print 'change path according to the system\ndeal with windows and non-windows'
    print 'some tests, run on windows, still need some chance to run this on linux'
    testSysPath()
    print 'make a folderPath with ending / or \  '
    print 'some tests, run on windows, still need some chance to run this on linux'
    testFolderPath()
##    print 'test createPath'
##    testCreatePath()
    print systemSpliter()
    print 'testing createFile'
    createFile(u'莫阿a/喵.txt',debug=True)
    '''
    
    
    
