#!/usr/bin/env python3
"""
Returns a tuple of size two containing a start index and an end index
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing a start index and an end index corresponding
    to the range of indexes
    """
    start_of_index = (page - 1) * page_size
    end_of_index = start_of_index + page_size
    return (start_of_index, end_of_index)
