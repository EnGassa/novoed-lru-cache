import unittest
from ..lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(5)

    def testGetOneKey(self):
        self.assertEquals(self.cache.get('something'), None);

    def testSetOneKey(self):
        self.cache.set('something', 'more')
        value = self.cache.get('something')
        self.assertEqual('more', value)

if __name__ == '__main__':
    unittest.main()
