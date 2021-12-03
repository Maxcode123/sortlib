from typing import MutableSequence

from sortlib.base_sorter import BaseSorter
from sortlib.common.comparable import ComparableType


class InsertionSorter(BaseSorter):

    def sort(self, array: MutableSequence[ComparableType]) -> None:
        for i in range(len(array[1:])):
            i += 1
            j = i
            while (j > 0) and (self.less(array[j], array[j-1])):
                self.exchange(array, j, j-1)
                j -= 1
        return None 