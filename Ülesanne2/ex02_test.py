import pytest
import ex02_solution


def test_examples():
    assert ex02_solution.find_amount_of_smaller_numbers([0, 3, 5, 2]) == [0, 2, 3, 1]
    assert ex02_solution.find_amount_of_smaller_numbers([1, 2, 3]) == [0, 1, 2]
    assert ex02_solution.find_amount_of_smaller_numbers([5, 2, 4, 5, 1]) == [3, 1, 2, 3, 0]
    assert ex02_solution.find_amount_of_smaller_numbers([3, 3, 3]) == [0, 0, 0]


def test_negative_nums():
    assert ex02_solution.find_amount_of_smaller_numbers([0, -3, -5, -2]) == [3, 1, 0, 2]
    assert ex02_solution.find_amount_of_smaller_numbers([-1, 2, 3]) == [0, 1, 2]
    assert ex02_solution.find_amount_of_smaller_numbers([-5, 2, -4, 5, 1]) == [0, 3, 1, 4, 2]
    assert ex02_solution.find_amount_of_smaller_numbers([3, -3]) == [2, 0]


def test_multiple_same_nums():
    assert ex02_solution.find_amount_of_smaller_numbers([0, -3, -3, 2, 2]) == [2, 0, 0, 3, 3]
    assert ex02_solution.find_amount_of_smaller_numbers([-1, 9, 9, 2, 9, 9, 9, -8, -1]) == [1, 4, 4, 3, 4, 4, 4, 0, 1]
    assert ex02_solution.find_amount_of_smaller_numbers([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
