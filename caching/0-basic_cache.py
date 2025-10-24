#!/usr/bin/python3

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
        
    def get(self, key):
        val = self.cache_data.get(key)
        if val:
            return self.cache_data[key]
        else:
            return None
        