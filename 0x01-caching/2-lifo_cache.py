#!/usr/bin/env python3
"""
This module implements a LIFO caching system that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This class implements a LIFO caching system.
    """

    def __init__(self):
        """
        Initialize the class and call the parent init method.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item in the cache using LIFO principle.
        If key or item is None, this method should not do anything.
        If the cache exceeds the max number of items,
        discard the most recently added item.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.last_key = key

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or
        if the key doesn’t exist in self.cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
