import unittest
import search


class TestSearch (unittest.TestCase):
    def test_request(self):
        w = '豚肉'
        s = search.SearchCookin(w)
        s.request_cookin()
        self.assertIsNotNone(s.soup)

if __name__ == "__main__":
    unittest.main()
