#!/usr/bin/env python3
"""
Defines a Cache class
"""
import sys
import redis
from uuid import uuid4
from typing import Union, Optional, Callable, Any


class Cache():
    """Represents a Cache class
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

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
