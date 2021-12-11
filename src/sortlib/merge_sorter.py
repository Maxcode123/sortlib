from typing import MutableSequence

from sortlib.base_sorter import BaseSorter
from sortlib.common.comparable import ComparableType


class MergeSorter(BaseSorter):

    def top_down_sort(self, array: MutableSequence[ComparableType]) -> None:
        self.__sort(array, 0, len(array) - 1)
        return None

    def bottom_up_sort(self, array: MutableSequence[ComparableType]) -> None:
        n = len(array)
        length = 1
        while (length < n):
            lo = 0
            while (lo < n - length):
                self.merge(array, lo, lo+length-1, min(lo+2*length-1, n-1))
                lo += 2*length
            length *= 2
        return None

    def __sort(self, array: MutableSequence[ComparableType], lo: int, hi: int) -> None:
        if (hi <= lo):
            return None
        mid = lo + (hi - lo)//2
        self.__sort(array, lo, mid)
        self.__sort(array, mid+1, hi)
        self.merge(array, lo, mid, hi)
        return None