#!/usr/bin/env python3
"""
This module implements an LRU caching system that inherits from BaseCaching.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    This class implements an LRU (Least Recently Used) caching system.
    """

    def __init__(self):
        """
        Initialize the class and call the parent init method.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache using LRU principle.
        If key or item is None, this method should not do anything.
        If the cache exceeds the max number of items,
        discard the least recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or
        if the key doesn’t exist in self.cache_data.
        """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
