from unittest import TestCase

import numpy as np

from src.sum_array_markbassem.sum_array import sum_array


class Test(TestCase):
    def test_sum_array(self):
        array1 = np.array([1, 2, 3, 4])
        array2 = np.array([5, 6, 7, 8])
        expected_res = sum_array(array1, array2)
        real = np.array([6, 8, 10, 12])
        assert all(expected_res == real)
