#!/usr/bin/env python3
'''Exercise File'''
import redis
import uuid

class Cache():
    '''Redis Cache Class'''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        '''Redis Cache store method'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
