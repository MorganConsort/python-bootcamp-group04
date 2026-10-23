"""W2-4: Cross-testing for thinh_nq's Week 1 homework.

Covers W1-1 (grades), W1-2 (text_tools), W1-3 (rules),
W1-4 (translate: transpose & insertion_sort), and W1-5 (timetable),
including edge cases not covered by instructor tests.
"""

import pytest
from members.thinh_nq.w1 import grades, rules, text_tools, timetable, translate


# ============================================================================
# W1-4: Translate (personal variant: matrix transpose & insertion_sort)
# ============================================================================


def test_transpose_square_and_rectangular():
    # 2x3 matrix
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert translate.transpose(matrix) == expected

    # 3x3 square matrix
    square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert translate.transpose(square) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


def test_transpose_single_row_and_single_column():
    # Single row (1x4) -> 4x1
    assert translate.transpose([[10, 20, 30, 40]]) == [[10], [20], [30], [40]]

    # Single column (4x1) -> 1x4
    assert translate.transpose([[10], [20], [30], [40]]) == [[10, 20, 30, 40]]


def test_transpose_empty_matrix():
    assert translate.transpose([]) == []


def test_insertion_sort_in_place_and_correctness():
    data = [9, -2, 5, 0, 7, 1]
    res = translate.insertion_sort(data)
    # Checks both return value and in-place sorting
    assert res == [-2, 0, 1, 5, 7, 9]
    assert data == [-2, 0, 1, 5, 7, 9]


def test_insertion_sort_edge_cases():
    assert translate.insertion_sort([]) == []
    assert translate.insertion_sort([42]) == [42]
    assert translate.insertion_sort([5, 5, 5]) == [5, 5, 5]


# ============================================================================
# W1-1: Grade summary (grades.py)
# ============================================================================


def test_grades_summary_even_and_odd_count():
    # Odd count
    assert grades.summary([8.0, 7.0, 9.0]) == {
        "min": 7.0,
        "max": 9.0,
        "mean": 8.0,
        "median": 8.0,
    }
    # Even count with fractional rounding
    res = grades.summary([7.5, 9.0, 6.0, 8.0])
    assert res == {"min": 6.0, "max": 9.0, "mean": 7.62, "median": 7.75}


def test_grades_summary_single_element_and_decimals():
    res = grades.summary([8.125])
    assert res["min"] == 8.125
    assert res["max"] == 8.125
    assert res["mean"] == 8.12
    assert res["median"] == 8.12


def test_grades_summary_empty_raises_value_error():
    with pytest.raises(ValueError):
        grades.summary([])


# ============================================================================
# W1-2: Word counter & top-k (text_tools.py)
# ============================================================================


def test_word_count_case_and_punctuations():
    text = "Hello, world! HELLO... world? World; hello:"
    counts = text_tools.word_count(text)
    assert counts == {"hello": 3, "world": 3}


def test_top_k_ordering_frequency_then_alphabetical():
    text = "banana apple apple orange orange orange banana cherry"
    # orange: 3, apple: 2, banana: 2, cherry: 1
    # ties between apple and banana -> apple comes before banana
    assert text_tools.top_k(text, 3) == [
        ("orange", 3),
        ("apple", 2),
        ("banana", 2),
    ]


def test_top_k_k_larger_than_unique_words_and_zero():
    text = "hello world"
    assert text_tools.top_k(text, 10) == [("hello", 1), ("world", 1)]
    assert text_tools.top_k(text, 0) == []
    assert text_tools.top_k(text, -2) == []


# ============================================================================
# W1-3: Thesis eligibility (rules.py)
# ============================================================================


@pytest.mark.parametrize(
    "credits,gpa,expected",
    [
        (120, 2.0, True),
        (119, 2.0, False),
        (120, 1.99, False),
        (150, 3.8, True),
        (0, 0.0, False),
    ],
)
def test_can_register_thesis_boundary(credits, gpa, expected):
    assert rules.can_register_thesis(credits, gpa) is expected


def test_missing_reasons_singular_and_plural():
    # Singular credit edge case ("need 1 more credit")
    reasons_1 = rules.missing(119, 2.5)
    assert reasons_1 == ["need 1 more credit"]

    # Plural credits + GPA
    reasons_2 = rules.missing(110, 1.8)
    assert len(reasons_2) == 2
    assert "need 10 more credits" in reasons_2
    assert any("2.0" in r for r in reasons_2)

    # Fully eligible -> empty list
    assert rules.missing(125, 3.0) == []


# ============================================================================
# W1-5: Timetable (timetable.py)
# ============================================================================


def test_by_day_grouping_and_sorting():
    items = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
        ("PHY00001", "Tue"),
    ]
    res = timetable.by_day(items)
    assert res == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003", "PHY00001"],
    }


def test_by_day_empty_and_preserves_input():
    items = [("B", "Mon"), ("A", "Mon")]
    original = list(items)
    timetable.by_day(items)
    assert items == original
    assert timetable.by_day([]) == {}
