import unittest
from search import *

class TestSearch (unittest.TestCase):
	def test_request():
		w = '豚肉'
		s = SearchCookin(w)
		self.assertIsNotNone(s.soup)
