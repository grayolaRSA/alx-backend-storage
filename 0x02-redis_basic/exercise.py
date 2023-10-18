#!/usr/bin/env python3
"""module for Cache redis class"""


import uuid
import redis
from typing import Union, Optional, Callable


class Cache:
    """class for Redis database"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
    
    def get(self, key: str, fn: Optional[Callable[..., None]] = None) -> Union[bytes, str, int]:

        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data
        
    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))
         
    
    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)