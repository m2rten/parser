import unittest
from conf import conf

class TestStringMethods(unittest.TestCase):

	def test_reading(self):
		cf = conf()
		self.assertEqual(cf.getConfObject("Logging","errorlog"), '../logs/error.log2')

	def test_autosetting(self):
		cf = conf()
		self.assertEqual(cf.url, 'http://www.postimees.ee')	
	
	def test_singleton_conf_creation(self):
		cf = conf(confFile="testconf.ini")
		cf2 = conf(confFile="nottest.ini")
		self.assertEqual(cf.url, cf2.url)
	  
if __name__ == '__main__':
	unittest.main()