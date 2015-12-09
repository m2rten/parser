# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata, time

url="http://www.postimees.ee"
##url= input ('ENTER - ')	

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('h1')
#headings = soup.findall("h1", { "class" : "frontHeading" }) 
i=0
p=0
tm= time.strftime("%H:%M:%S")
dt=time.strftime("%d/%d/%Y")

def removeComments (sentence):
	return sentence

with open('test.csv', 'a') as f:
		
	for tag in tags:
		i+=1
		try:
			for string in tag.strings:
				##print (bytes(string, 'utf-8').decode("utf-8"))
				string = removeComments(string)
				f.write(string.strip() )
			f.write(";"+str(i)+";"+ str(dt)+";"+ tm+";"+"\n")
		except UnicodeEncodeError:
			p+=1			
			print ("jama")
print (str(i) + " korda")	
print (str(p) + " probleemi")

'''
for heading in headings:
	print (heading)
'''