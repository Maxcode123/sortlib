from typing import List

import pytest

from sortlib.insertion_sorter import InsertionSorter
from sortlib.selection_sorter import SelectionSorter
from sortlib.shell_sorter import ShellSorter


class TestSorters:

    @pytest.fixture
    def array(self) -> List[int]:
        return [0, 100, -12, -5, 1, 2, -180, -30, -50, 20, 9, -1]

    @pytest.fixture
    def sorted_array(self) -> List[int]:
        return [-180, -50, -30, -12, -5, -1, 0, 1, 2, 9, 20, 100]


    def test_insertion_sorter(self, array, sorted_array):
        InsertionSorter().sort(array)
        assert array == sorted_array
    
    def test_selection_sorter(self, array, sorted_array):
        SelectionSorter().sort(array)
        assert array == sorted_array

    def test_shell_sorter(self, array, sorted_array):
        ShellSorter().sort(array)
        assert array == sorted_array