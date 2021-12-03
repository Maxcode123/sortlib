from typing import MutableSequence

from sortlib.common.comparable import ComparableType


class BaseSorter:
    

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

    def merge(self, array: MutableSequence[ComparableType], lo: int, mid: int, hi: int) -> None:
        'Merges array[lo:mid] with array[mid+1:hi]'
        i = lo
        j = mid + 1
        aux = [0] * len(array)
        for k in range(lo, hi+1):
            aux[k] = array[k]
        for k in range(lo, hi+1):
            if (i > mid):
                array[k] = aux[j]
                j += 1
            elif (j > hi):
                array[k] = aux[i]
                i += 1
            elif (self.less(aux[j], aux[i])):
                array[k] = aux[j]
                j += 1
            else:
                array[k] = aux[i]
                i += 1
        return None