#coding: utf-8
from sysPath import folderPath,sysPath
import glob
import os,codecs

def combineTXT(folder,des='combine.txt'):
    folder=folderPath(folder)
    des=sysPath(des)
    g=codecs.open(des,'w','gb18030')
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith('.txt'):
                add=sysPath(root+'/'+f)
                fi=codecs.open(add,'r','gb18030')
                g.write(fi.read())
    g.close()

folder='C:\Dropbox\downloads/a\ '[:-1]

combineTXT(folder=folder)
