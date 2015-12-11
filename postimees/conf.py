import sys, configparser

class conf:
	
	def __init__(self, confFile="conf.ini"):
		global config 
		config = configparser.ConfigParser()
		config.read(confFile)
		self.setValues()
		
	def setValues(self):
		self.url = config["General"]["url"]
		
	def getConfObject(self, section, item):
		return config[section][item]

