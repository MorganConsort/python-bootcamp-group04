"""W2-4: Minh reviews Thang, following dat -> dang -> minh -> thang.

Test Thang's W1-4 translation, including boundaries absent from instructor tests.
"""

import pytest

from members.tranquyetthang27.w1.translate import primes_up_to


def test_empty_range():
    assert primes_up_to(0) == []


def test_negative_bound():
    assert primes_up_to(-10) == []


def test_smallest_prime_is_included():
    assert primes_up_to(2) == [2]


def test_prime_upper_bound_is_included():
    assert primes_up_to(13)[-1] == 13


@pytest.mark.parametrize("square", [4, 9, 25, 49, 121])
def test_prime_squares_are_not_primes(square):
    assert square not in primes_up_to(square)


def test_larger_range_matches_trial_division():
    expected = [n for n in range(2, 201) if all(n % d for d in range(2, n))]
    assert primes_up_to(200) == expected


def test_repeated_calls_are_independent():
    first = primes_up_to(10)
    first.append(99)
    assert primes_up_to(3) == [2, 3]
    assert primes_up_to(10) == [2, 3, 5, 7]
