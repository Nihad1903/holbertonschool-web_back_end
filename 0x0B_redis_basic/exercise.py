#!/usr/bin/env python3
"""
exercise.py

This module provides a Cache class that wraps Redis operations.
It supports storing data, retrieving data with optional conversion,
counting method calls, and recording call history.
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
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a method.

    Inputs are stored in a Redis list under "<qualname>:inputs"
    Outputs are stored in a Redis list under "<qualname>:outputs"
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store input arguments
        self._redis.rpush(input_key, str(args))

        # Execute the original method
        result = method(self, *args, **kwargs)

        # Store output
        self._redis.rpush(output_key, result)

        return result

    return wrapper


class Cache:
    """
    Cache class for interacting with a Redis datastore.

    Provides methods to store data, retrieve data, count calls,
    and record input/output history.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance.

        Creates a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
        Retrieve data from Redis by key with optional conversion.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a UTF-8 decoded string from Redis.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.
        """
        return self.get(key, fn=int)

    def replay(method: Callable) -> None:
        """
        Display the history of calls of a particular Cache method.
    Shows how many times the method was called along with
        the inputs and outputs of each call.
        """
        redis_instance = method.__self__._redis
        method_name = method.__qualname__

        # Get call count
        calls = redis_instance.get(method_name)
        calls = int(calls) if calls else 0

        print(f"{method_name} was called {calls} times:")

        # Get inputs and outputs history
        inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
        outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)

        # Display history
        for inp, out in zip(inputs, outputs):
            print(
                f"{method_name}(*{inp.decode('utf-8')}) -> "
                f"{out.decode('utf-8')}"
            )
