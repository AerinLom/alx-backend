#!/usr/bin/env python3
"""
This module inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class is a basic caching system without any limit.
    """

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or if the key
        doesn’t exist in self.cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
