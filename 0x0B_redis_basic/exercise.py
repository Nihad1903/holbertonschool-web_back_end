#!/usr/bin/env python3
'''Exercise File'''
import redis
import uuid
from typing import Union, Callable, Optional, Any

class Cache():
    '''Redis Cache Class'''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Redis Cache store method'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Any]] = None
    ) -> Any:
        """
        Retrieve data from Redis by key.

        Optionally applies a conversion function to the retrieved
        byte string.

        Args:
            key (str): The Redis key.
            fn (Optional[Callable[[bytes], Any]]): A callable used to
                convert the retrieved value.

        Returns:
            Any: The retrieved value, optionally converted, or None
            if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis.

        Args:
            key (str): The Redis key.

        Returns:
            Optional[str]: The decoded UTF-8 string or None if the key
            does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.

        Args:
            key (str): The Redis key.

        Returns:
            Optional[int]: The integer value or None if the key
            does not exist.
        """
        return self.get(key, fn=int)
