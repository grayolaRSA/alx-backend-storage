#!/usr/bin/env python3
"""module for Cache redis class"""


import uuid
import redis
from typing import Union


class Cache:
    """class for Redis database"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
    