import pytest

from members.man_lpd.w1.translate import binary_search


def test_empty_list():
    assert binary_search([], 10) == -1


def test_single_element_found():
    assert binary_search([42], 42) == 0


def test_single_element_not_found_smaller():
    assert binary_search([42], 10) == -1


def test_single_element_not_found_larger():
    assert binary_search([42], 100) == -1


def test_two_elements():
    arr = [10, 20]
    assert binary_search(arr, 10) == 0
    assert binary_search(arr, 20) == 1
    assert binary_search(arr, 5) == -1
    assert binary_search(arr, 15) == -1
    assert binary_search(arr, 25) == -1


def test_first_element():
    arr = [1, 3, 5, 7, 9, 11]
    assert binary_search(arr, 1) == 0


def test_last_element():
    arr = [1, 3, 5, 7, 9, 11]
    assert binary_search(arr, 11) == 5


def test_middle_element_odd_length():
    arr = [2, 4, 6, 8, 10]
    assert binary_search(arr, 6) == 2


def test_middle_element_even_length():
    arr = [2, 4, 6, 8]
    assert binary_search(arr, 4) == 1
    assert binary_search(arr, 6) == 2


def test_target_missing_between_elements():
    arr = [1, 5, 10, 15, 20]
    assert binary_search(arr, 7) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 25) == -1


def test_negative_numbers():
    arr = [-30, -15, -5, 0, 8, 14]
    assert binary_search(arr, -30) == 0
    assert binary_search(arr, -5) == 2
    assert binary_search(arr, 0) == 3
    assert binary_search(arr, 14) == 5
    assert binary_search(arr, -10) == -1


def test_large_sorted_list():
    arr = list(range(0, 2000, 2))
    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 1998) == 999
    assert binary_search(arr, 1000) == 500
    assert binary_search(arr, 1001) == -1


def test_list_not_mutated():
    original = [2, 4, 6, 8, 10]
    copy = original.copy()
    binary_search(original, 6)
    binary_search(original, 7)
    assert original == copy


@pytest.mark.parametrize("target", [1, 3, 7, 9, 13, 17, 19, 23])
def test_all_elements_present_found(target):
    arr = [1, 3, 7, 9, 13, 17, 19, 23]
    idx = binary_search(arr, target)
    assert arr[idx] == target
