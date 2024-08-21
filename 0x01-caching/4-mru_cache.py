#!/usr/bin/env python3
"""
This module inherits from BaseCaching and is a caching system
using the MRU (Most Recently Used) algorithm.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    This class is a caching system that uses the MRU
    (Most Recently Used) algorithm.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        discard the most recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recent_key = self.order.pop()
                del self.cache_data[most_recent_key]
                print(f"DISCARD: {most_recent_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or if the key
        doesn’t exist in self.cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
