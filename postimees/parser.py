# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata, time, re
from conf import conf
import sys

cf = conf()

url=cf.url

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('h1')

i=0
p=0
tm= time.strftime("%H:%M:%S")
dt=time.strftime("%d/%d/%Y")


def removeComments (sentence):
	p = re.compile("(.*[^0-9])(\(\d+\)|\d+)$")
	m = p.match(sentence)
	if m:
		return m.group(1)
	else:
		return sentence

with open('test.csv', 'a') as f:
		
	for tag in tags:
		i+=1
		heading = ""
		try:
			for string in tag.strings:
				##print (bytes(string, 'utf-8').decode("utf-8"))
				##print (string)				
				heading+=string.strip() 
			heading = removeComments(heading)
			f.write(heading + ";"+str(i)+";"+ str(dt)+";"+ tm+";"+"\n")
		except UnicodeEncodeError:
			p+=1			
			print ("jama")
print (str(i) + " korda")	
print (str(p) + " probleemi")

'''
for heading in headings:
	print (heading)
'''