import pytest
import ex01_solution


def test_examples():
    assert ex01_solution.string_with_best_score(["I", "love", "Python"]) == "love"
    assert ex01_solution.string_with_best_score(["ABC", "abc"]) == "abc"
    assert ex01_solution.string_with_best_score(["Hello", "Python"]) == "Python"
    assert ex01_solution.string_with_best_score(["aaa", "yyy", "bbb"]) == "yyy"


def test_multiple_best_scores():
    assert ex01_solution.string_with_best_score(["abb", "ABC", "bba"]) == "abb"
    assert ex01_solution.string_with_best_score(["bba", "ABC", "abb"]) == "bba"


def test_empty_list():
    assert ex01_solution.string_with_best_score([]) == ""


def test_empty_list_2():
    assert ex01_solution.string_with_best_score(["", " "]) == ""
    assert ex01_solution.string_with_best_score([""]) == ""
    assert ex01_solution.string_with_best_score(["  ", " "]) == ""
    assert ex01_solution.string_with_best_score(["  ", " ", "   "]) == ""
