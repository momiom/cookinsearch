import unittest
import search

class TestSearch (unittest.TestCase):
	def test_request():
		w = '豚肉'
		s = search.SearchCookin(w)
		self.assertIsNotNone(s.soup)
