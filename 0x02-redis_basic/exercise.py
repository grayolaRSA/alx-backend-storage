#!/usr/bin/env python3
"""module for Cache redis class"""


import uuid
import redis
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator function for store method to count calls"""
    @wraps(method)
    def wrapper(self, data: Union[bytes, str, int, float]) -> str:
        data_key = method.__qualname__
        self._redis.incr(data_key)
        result = method(self, data)
        return result

    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator method for store method to create call history"""
    @wraps(method)
    def decorator(self, *args, **kwargs):
        input = f"{method.__qualname__}:inputs"
        output = f"{method.__qualname__}:outputs"
        self._redis.rpush(input, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output, result)
        return result

    return decorator


def replay(method: Callable) -> None:
    """method to replay calls made to cache methods"""
    meth_name = method.__qualname__
    input_key = f"{meth_name}:inputs"
    output_key = f"{meth_name}:outputs"

    r = redis.Redis()

    inputs = r.lrange(input_key, 0, -1)
    outputs = r.lrange(output_key, 0, -1)

    count = r.get(meth_name)
    if count is None:
        count = 0
    else:
        count = int(count)

    print(f"{meth_name} was called {count} times:")

    for (input_data, output_data) in zip(inputs, outputs):
        print(f"{meth_name}(*{input_data.decode('utf-8')}) -> "
              f"{output_data.decode('utf-8')}")


class Cache:
    """class for Redis database"""

    def __init__(self):
        """init method for cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[bytes, str, int, float]) -> str:
        """method to store data to redis"""

        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self,
            key: str, fn: Optional[Callable[..., None]]
            = None) -> Union[bytes, str, int]:
        """class method to get values of db data"""

        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """sub method of get method for strings"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """sub method of get method for integers"""
        return self.get(key, fn=int)
