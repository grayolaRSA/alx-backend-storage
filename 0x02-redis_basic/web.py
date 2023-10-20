#!/usr/bin/env python3
"""module for requesting web pages"""

import datetime
import redis
import requests
from typing import Callable
from functools import wraps
from exercise import count_calls, Cache, call_history


def expire(method: Callable) -> None:
    """decorator function for clearing cache"""
    @wraps(method)
    def wrapper(url: str) -> str:
        r = redis.Redis()
        cache = set()

        cached_content = r.get(url)
        if cached_content:
            print(f"served cached content")
            return cached_content.decode('utf-8')
        else:
            results = method(url)
            now = datetime.datetime.utcnow()
            addrts = f"{url}:{now.minute}"
            cache.add(addrts)
            n = r.incr(addrts, 1)
            print(n)
        _ = r.expire(addrts, 10)
        return results

    return wrapper

@expire
def get_page(url: str) -> str:
    """method to get web page"""

    response = requests.get(url)

    if response.status_code == 200:
        page_content = response.text

        return page_content

    else:
        raise Exception(f"Failed to fetch page: {url}")

if __name__ == '__main__':
    url = "http://slowwly.robertomurray.co.uk"
    content = get_page(url)
    print(content)