#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import Dict, List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes a new Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                content = [row for row in reader]
            self.__dataset = content[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            data = self.dataset()
            truncated_data = data[:1000]
            self.__indexed_dataset = {
                index: data[index] for index in range(len(data))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves info about a page from a given index and with a
        specified size.
        """
        i_data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(i_data.keys())

        page_content = []
        item_count = 0
        next_index = None
        start_index = index if index is not None else 0

        for i, item in i_data.items():
            if i >= start_index and item_count < page_size:
                page_content.append(item)
                item_count += 1
                continue
            if item_count == page_size:
                next_index = i
                break

        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_content),
            'data': page_content,
        }
        return page_info
