import unittest
from conf import conf

class TestStringMethods(unittest.TestCase):

	def test_reading(self):
		cf = conf()
		self.assertEqual(cf.getConfObject("Logging","errorfile"), 'error.log')

	def test_autosetting(self):
		cf = conf()
		self.assertEqual(cf.url, 'http://www.postimees.ee')	
	  
if __name__ == '__main__':
	unittest.main()