# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata, time, re
from conf import conf
from database import database
import sys
import csv

class postimeesParser:
	def removeComments (self, sentence):
		p = re.compile("(.*[^0-9])(\(\d+\)|\d+)$")
		m = p.match(sentence)
		if m:return m.group(1)
		else:return sentence
			
	def parse(self, html, db, cf=None, dt=None, tm=None):
		soup = BeautifulSoup(html, "html.parser")
		counter={"total":0, "errors":0}
		output=cf.getConfObject("General","results_folder") +"/" + cf.getConfObject("General","output_file")
		
		if not dt: dt=time.strftime("%d/%m/%Y")
		if not tm: tm= time.strftime("%H:%M:%S")
		
		db.connect()
		tags = soup('h1')
		with open(output, 'a', encoding="utf-8", newline="") as csvfile:	
			writer = csv.writer(csvfile, delimiter=';')
			for tag in tags:
				counter["total"]+=1
				try:	
					heading = self.removeComments("".join([string.strip() for string in tag.strings]))
					writer.writerow([heading, str(counter["total"]), dt, tm])
					print (dt)
					db.insertHeading(heading, str(counter["total"]), dt, tm)
				except UnicodeEncodeError:
					counter["errors"]+=1			
					print ("jama")
		db.close()
		return counter		

if __name__ == '__main__':
	cf = conf()
	url=cf.url
	db = database(cf)
	html = urlopen(url).read()
	pmparser = postimeesParser()
	counter = pmparser.parse(html, db, cf=cf)
	
					
	print (str(counter["total"]) + " korda")	
	print (str(counter["errors"]) + " probleemi")
