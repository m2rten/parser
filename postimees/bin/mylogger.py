import logging
from singleton import Singleton
from conf import conf

class MyLogger(metaclass=Singleton):
	
	def __init__(self):
		cf = conf()
		logging.basicConfig(filename=cf.getConfObject("Logging","infolog"),format='%(asctime)s %(message)s',level=logging.INFO)
		logging.info('Logging initializes')
	
log = MyLogger()