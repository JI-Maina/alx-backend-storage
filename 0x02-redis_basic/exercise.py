#!/usr/bin/env python3
"""

"""
import redis
from uuid import uuid1
from typing import Any


class Cache():
    """
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self: redis.client.Redis, data: Any) -> str:
        """takes a data argument, sets it db and returns a storage key"""

        key = str(uuid1())

        self._redis.set(key, data)

        return key
