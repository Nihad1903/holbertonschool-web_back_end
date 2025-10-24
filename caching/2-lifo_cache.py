#!/usr/bin/python3
'''LIFO Cache'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO Caching class'''
    def put(self, key, item):
        '''LIFO cache put function'''
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[-1]
                print("DISCARD:", first_key)
                del self.cache_data[first_key]

    def get(self, key):
        '''LIFO cache get function'''
        val = self.cache_data.get(key)
        if val:
            return self.cache_data[key]
        else:
            return None
