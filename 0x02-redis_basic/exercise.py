#!/usr/bin/env python3
"""
Defines a Cache class
"""
import sys
import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Optional, Callable, Any


def count_calls(fn: Callable) -> Callable:
    """
    """

    key = fn.__qualname__

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """
        """
        self._redis.incr(key)
        return fn(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    """
    """
    key1 = method.__qualname__ + ":inputs"
    key2 = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        """
        """
        self._redis.rpush(key1, str(args))
        x = method(self, *args)
        self._redis.rpush(key2, x)
        return x

    return wrapper

class Cache():
    """Represents a Cache class
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument, sets it db and returns a storage key"""

        key = str(uuid4())

        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Retrieves converted value"""
        if fn:
            return fn(self._redis.get(key))

        value = self._redis.get(key)
        return value

    def get_int(self: bytes) -> int:
        """returns a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """returns a string"""
        return self.decode("utf-8")
