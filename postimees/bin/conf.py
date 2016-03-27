import sys, configparser
from singleton import Singleton

class conf(metaclass=Singleton):
	
	def __init__(self, confFile="conf.ini"):
		global config
		config = configparser.ConfigParser()
		config.read(confFile)
		self.setValues()
		
	def setValues(self):
		self.url = config["General"]["url"]
		self.host = config["Database"]["host"]
		self.dbname = config["Database"]["dbname"]
		self.user = config["Database"]["user"]
		self.password = config["Database"]["password"]
		
	def getConfObject(self, section, item):
		return config[section][item]

