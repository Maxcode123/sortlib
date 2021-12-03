from typing import MutableSequence

from sortlib.base_sorter import BaseSorter
from sortlib.common.comparable import ComparableType


class ShellSorter(BaseSorter):

    def sort(self, array: MutableSequence[ComparableType]) -> None:
        n = len(array)
        h = 1
        while (h < n/3):
            h = 3*h + 1
        while (h >= 1):
            for i in range(h, n):
                j = i
                while (j >= h) and (self.less(array[j], array[j-h])):
                    self.exchange(array, j , j-h)
                    j -= 1
                i += 1
            h = h//3
        return None 