import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        # Create cache of capacity 5
        self.cache = LRUCache(5)

    # Test getting a non-existent key
    def testGetOneKey(self):
        self.assertIsNone(self.cache.get('something'))

    # Test setting and getting 1 key
    def testSetOneKey(self):
        self.cache.set('something', 'more')
        value = self.cache.get('something')
        self.assertEqual('more', value)

    # Test inserting 1 more than the capacity and the purging of the least
    # recently used item
    def testPurgeLRU(self):
        # Set 5 value
        for i in range(1, 6):
            self.cache.set(str(i), i)
        # Get the 5 values in order
        for i in range(1, 6):
            self.cache.get(str(i))
        # Set value beyond capacity
        self.cache.set(str(6), 6)
        self.assertIsNone(self.cache.get('1'))

    # Test inserting 2x elements of the capacity and the first half of elements
    # should be purged
    def testPurgeOldestCached(self):
        # Insert 2x of the capacity
        for i in range(1, 11):
            self.cache.set(str(i), i)
        # Check the oldest elements inserted, they should be purged
        for i in range(1, 6):
            self.assertIsNone(self.cache.get(str(i)))
        for i in range(6, 11):
            self.assertIsNotNone(self.cache.get(str(i)))

    # Test clearing of the cache
    def testClearingCache(self):
        for i in range(1, 6):
            self.cache.set(str(i), i)
        for i in range(1, 6):
            self.assertEqual(self.cache.get(str(i)), i)
        self.cache.clear()
        for i in range(1, 6):
            self.assertIsNone(self.cache.get(str(i)))

    # Test inserting a pre-existing key and updating its value in the cache
    def testInsertingExistingKey(self):
        for i in range(1, 6):
            self.cache.set(str(i), i)
        self.cache.set('3', 'abcdef')
        self.assertEqual(self.cache.get('3'), 'abcdef')

if __name__ == '__main__':
    unittest.main()
