from typing import MutableSequence

from sortlib.common.comparable import ComparableType


class BaseSorter:
    """
    Base sorter class, all other sorters inherit from this class.
    Implements the methods less, exchange, show and is_sorted.
    """

    @staticmethod
    def less(v: ComparableType, w: ComparableType) -> bool:
        'Return true if v is lower than w'
        return v < w

    @staticmethod
    def exchange(array: MutableSequence[ComparableType], i: int, j: int) -> None:
        'Exchange items of array with indices i and j'
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        return None

    @staticmethod
    def show(array: MutableSequence[ComparableType]) -> None:
        'Print items in array'
        for item in array:
            print(item)
        return None

    def is_sorted(self, array: MutableSequence[ComparableType]) -> bool:
        'Return true if array is sorted'
        for index in range(len(array[1:])):
            index += 1
            if self.less(array[index], array[index-1]):
                return False
            return True