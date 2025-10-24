#!/usr/bin/python3
'''FIFO Cache'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO Caching Class'''    
    def put(self, key, item):
        '''FIFO caching put function'''
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                print("DISCARD:", first_key)
                del self.cache_data[first_key]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        '''Basic cache get function'''
        val = self.cache_data.get(key)
        if val:
            return self.cache_data[key]
        else:
            return None
