#!/usr/bin/env python3
"""
cache.py

This module provides a Cache class that wraps basic Redis operations.
It supports storing data, retrieving data with optional type conversion,
and counting how many times cache methods are called.
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a Cache method is called.

    The count is stored in Redis using the method's qualified name
    as the key.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The wrapped method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count
        and executes the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Cache class for interacting with a Redis datastore.

    Provides methods to store data, retrieve data with optional
    conversion, and track method call counts.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance.

        Creates a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The generated Redis key.
        """
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

        Optionally applies a conversion function.

        Args:
            key (str): The Redis key.
            fn (Optional[Callable[[bytes], Any]]): Conversion function.

        Returns:
            Any: The retrieved value or None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a UTF-8 decoded string from Redis.

        Args:
            key (str): The Redis key.

        Returns:
            Optional[str]: The decoded string or None.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.

        Args:
            key (str): The Redis key.

        Returns:
            Optional[int]: The integer value or None.
        """
        return self.get(key, fn=int)
