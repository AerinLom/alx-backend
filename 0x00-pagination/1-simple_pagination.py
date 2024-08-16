#!/usr/bin/env python3
"""
Returns a tuple of size two containing a start index and an end index
"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing a start index and an end index corresponding
    to the range of indexes
    """
    start_of_index = (page - 1) * page_size
    end_of_index = start_of_index + page_size
    return (start_of_index, end_of_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a list of rows for the requested page and page_size.
        """
        assert isinstance(page, int) and page > 0, (
            "Page number must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer"
        )
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
