#!/usr/bin/env python3
"""
This module implements a FIFO caching system that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class implements a FIFO caching system.
    """

    def __init__(self):
        """
        Initialize the class and call the parent init method.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO principle.
        If key or item is None, this method should not do anything.
        If the cache exceeds the max number of items, discard the oldest entry.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or
        if the key doesn’t exist in self.cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
