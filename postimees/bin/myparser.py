# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata, time, re
from conf import conf
import sys
import csv

class postimeesParser:
	def removeComments (self, sentence):
		p = re.compile("(.*[^0-9])(\(\d+\)|\d+)$")
		m = p.match(sentence)
		if m:return m.group(1)
		else:return sentence
			
	def parse(self, html, cf=None, dt=None, tm=None):
		soup = BeautifulSoup(html, "html.parser")
		counter={"total":0, "errors":0}
		output=cf.getConfObject("General","results_folder") +"/" + cf.getConfObject("General","output_file")
		
		if not dt: dt=time.strftime("%d/%m/%Y")
		if not tm: tm= time.strftime("%H:%M:%S")
		
		tags = soup('h1')
		with open(output, 'a', encoding="utf-8", newline="") as csvfile:	
			writer = csv.writer(csvfile, delimiter=';')
			for tag in tags:
				counter["total"]+=1
				try:	
					heading = self.removeComments("".join([string.strip() for string in tag.strings]))
					writer.writerow([heading, str(counter["total"]), dt, tm])
				except UnicodeEncodeError:
					counter["errors"]+=1			
					print ("jama")
		return counter		

if __name__ == '__main__':
	cf = conf()
	url=cf.url
	html = urlopen(url).read()
	pmparser = postimeesParser()
	counter = pmparser.parse(html, cf=cf)
					
	print (str(counter["total"]) + " korda")	
	print (str(counter["errors"]) + " probleemi")
