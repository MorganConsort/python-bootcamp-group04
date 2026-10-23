"""W2-4: Minh reviews Thang, following dat -> dang -> minh -> thang.

Test Thang's W1-4 translation, including boundaries absent from instructor tests.
"""

import pytest

from members.tranquyetthang27.w1.translate import primes_up_to
from members.tranquyetthang27.w1 import grades, rules, text_tools, timetable, translate


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


def test_personal_assignment_sieve_api():
    """The personal W1-4 task explicitly requires sieve(n), not just an alias."""
    sieve = getattr(translate, "sieve", None)
    assert callable(sieve), "task-tqt.md requires sieve(n) -> list[int]; public API is missing"
    for bound, expected in [
        (-10, []),
        (0, []),
        (1, []),
        (2, [2]),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
    ]:
        assert sieve(bound) == expected


@pytest.mark.parametrize(
    "scores,expected",
    [
        ([8.125], {"min": 8.125, "max": 8.125, "mean": 8.12, "median": 8.12}),
        ([9, 1, 2], {"min": 1, "max": 9, "mean": 4.0, "median": 2}),
        ([10, 0, 8, 4], {"min": 0, "max": 10, "mean": 5.5, "median": 6.0}),
    ],
)
def test_grade_rounding_and_input_preservation(scores, expected):
    original = list(scores)
    assert grades.summary(scores) == expected
    assert scores == original


def test_empty_grades_raise_value_error():
    with pytest.raises(ValueError):
        grades.summary([])


def test_word_case_whitespace_and_punctuation():
    assert text_tools.word_count("Git, GIT.\ngit! Python? python;\tPYTHON:") == {
        "git": 3,
        "python": 3,
    }
    assert text_tools.word_count("It's well-known") == {"it's": 1, "well-known": 1}


@pytest.mark.parametrize("text", ["", " \n\t ", ". , ! ? ; :"])
def test_empty_word_inputs(text):
    assert text_tools.word_count(text) == {}
    assert text_tools.top_k(text, 3) == []


def test_top_k_ties_and_zero():
    assert text_tools.top_k("z b a z b c", 10) == [("b", 2), ("z", 2), ("a", 1), ("c", 1)]
    assert text_tools.top_k("a b", 0) == []


@pytest.mark.parametrize(
    "credits,gpa,eligible,reasons",
    [
        (120, 2.0, True, 0),
        (119, 2.0, False, 1),
        (120, 1.99, False, 1),
        (0, 0.0, False, 2),
        (150, 4.0, True, 0),
    ],
)
def test_thesis_boundaries(credits, gpa, eligible, reasons):
    assert rules.can_register_thesis(credits, gpa) is eligible
    assert len(rules.missing(credits, gpa)) == reasons


def test_timetable_duplicates_and_input_preservation():
    items = [("Z", "Mon"), ("A", "Mon"), ("Z", "Mon"), ("B", "Tue")]
    original = list(items)
    assert timetable.by_day(items) == {"Mon": ["A", "Z", "Z"], "Tue": ["B"]}
    assert items == original
    assert timetable.by_day([]) == {}
