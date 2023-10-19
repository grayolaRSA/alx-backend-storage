#!/usr/bin/env python3
"""module for requesting web pages"""

import redis
import requests
from typing import Callable
from functools import wraps
from exercise import count_calls, Cache, call_history


def expire(method: Callable) -> None:
    """decorator function for clearing cache"""
    @wraps(method)
    def wrapper(url: str) -> str:
        cache = Cache()
        results = method(url)
        cache.expire(results, 10)
        return results

    return wrapper


@expire
@call_history
@count_calls
def get_page(url: str) -> str:
    """method to get web page"""
    content = requests(url)
    return content
