from typing import MutableSequence

from sortlib.base_sorter import BaseSorter
from sortlib.common.comparable import ComparableType


class SelectionSorter(BaseSorter):
    
    def sort(self, array: MutableSequence[ComparableType]) -> None:
        for i in range(len(array)):
            min = i
            for j in range(i+1, len(array)):
                if self.less(array[j], array[min]):
                    min = j
            self.exchange(array, i, min)
        return None