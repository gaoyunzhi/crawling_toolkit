#coding: utf-8
import sys,binascii

def trans(file):
	f=open(file,'rb')
	i=0
	for chr in f.read():
		print chr,
		i+=1
		if i>3000: break
		if i%16==0: print

	f.close()
		
	
for f in sys.argv[1:]+['C:\Users\gyz\Desktop\\1\\1.kux']:
	trans(f)