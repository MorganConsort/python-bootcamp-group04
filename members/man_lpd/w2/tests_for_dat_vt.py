import pytest

from members.dat_vt.w1.grades import summary
from members.dat_vt.w1.rules import can_register_thesis, missing
from members.dat_vt.w1.text_tools import top_k, word_count
from members.dat_vt.w1.timetable import by_day
from members.dat_vt.w1.translate import binary_search


# test for W1-1 summary()
# integer results
def test_summary_evenNumberIntResults():
    assert summary([2, 4, 6, 8]) == {
        "min": 2,
        "max": 8,
        "mean": 5,
        "median": 5,
    }


# given case
def test_summary_givenCase():
    assert summary([7.5, 9, 6, 8]) == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


# rounding case
def test_summary_roundingCase():
    scores = [1.111, 2.222, 3.333, 4.444, 5.555, 6.666, 9.999]
    assert summary(scores) == {
        "min": 1.111,
        "max": 9.999,
        "mean": 4.76,
        "median": 4.44,
    }


# empty case
def test_summary_emptyListRaiseError():
    with pytest.raises(ValueError):
        summary([])


# test for W1-2 word_count() and top_k()
LONG_PARAGRAPH = """
Python helps students learn programming by turning ideas into small programs.
Students can read data, clean data, test data, and explain results with clear
code. Good tests help students find mistakes before those mistakes reach
users. A careful programmer writes simple functions, chooses clear names,
and checks unusual inputs. With regular practice, Python becomes easier,
testing becomes faster, and each new program becomes more reliable.
"""


# test for word_count()
def test_word_count_mixedCaseAndPunctuationResults():
    result = word_count("Git, git! Python? PYTHON; fun:")

    assert result == {
        "git": 2,
        "python": 2,
        "fun": 1,
    }


def test_word_count_emptyTextResults():
    assert word_count("") == {}


def test_word_count_onlyPunctuationResults():
    assert word_count("!!!...,,,???;;;::") == {}


def test_wordCount_realParagraphOverSixtyWordsResults():
    paragraph = LONG_PARAGRAPH
    result = word_count(paragraph)

    # General checks
    assert len(paragraph.split()) == 65
    assert sum(result.values()) == 65
    assert len(result) == 53

    # Repeated words
    assert result["python"] == 2
    assert result["students"] == 3
    assert result["data"] == 3
    assert result["and"] == 3
    assert result["with"] == 2
    assert result["clear"] == 2
    assert result["mistakes"] == 2
    assert result["becomes"] == 3

    # Words appearing once
    assert result["programming"] == 1
    assert result["programs"] == 1
    assert result["program"] == 1
    assert result["tests"] == 1
    assert result["testing"] == 1
    assert result["helps"] == 1
    assert result["help"] == 1
    assert result["reliable"] == 1
    assert result["unusual"] == 1

    # Case and punctuation handling
    assert "Python" not in result
    assert "Students" not in result
    assert "programs." not in result
    assert "data," not in result
    assert "practice," not in result
    assert "reliable." not in result


# test for top_k()
def test_top_k_longParagraphResults():
    result = top_k(LONG_PARAGRAPH, 5)
    assert result == [
        ("and", 3),
        ("becomes", 3),
        ("data", 3),
        ("students", 3),
        ("clear", 2),
    ]


def test_top_k_courseExampleResults():
    result = top_k("Git is fun. Git is fast!", 2)
    assert result == [
        ("git", 2),
        ("is", 2),
    ]


def test_top_k_equalCountsAlphabeticalResults():
    text = "zebra apple mango zebra apple mango kiwi"
    result = top_k(text, 3)
    assert result == [
        ("apple", 2),
        ("mango", 2),
        ("zebra", 2),
    ]


# test for W1-3 can_register_thesis() and missing()
def test_can_register_thesis_exactBoundaryResults():
    assert can_register_thesis(120, 2.0) is True


def test_can_register_thesis_aboveRequirementsResults():
    assert can_register_thesis(140, 3.5) is True


def test_can_register_thesis_insufficientCreditsResults():
    assert can_register_thesis(119, 3.5) is False


def test_can_register_thesis_insufficientGpaResults():
    assert can_register_thesis(130, 1.99) is False


def test_can_register_thesis_bothRequirementsMissingResults():
    assert can_register_thesis(100, 1.5) is False


def test_missing_noRequirementsMissingResults():
    assert missing(120, 2.0) == []


def test_missing_twoCreditsMissingResults():
    assert missing(118, 3.0) == ["need 2 more credits"]


def test_missing_bothRequirementsMissingResults():
    result = missing(100, 1.5)

    assert isinstance(result, list)
    assert len(result) == 2
    assert any("credits" in reason.lower() for reason in result)
    assert any(
        "gpa" in reason.lower() or "grade" in reason.lower() for reason in result
    )


# W1-4: Dat implements binary search, not greatest common divisor.
@pytest.mark.parametrize(
    "values, key, expected",
    [
        ([1, 3, 5, 7], 5, 2),
        ([1, 3, 5, 7], 4, -1),
        ([], 1, -1),
        ([1, 3, 5, 7], 1, 0),
        ([1, 3, 5, 7], 7, 3),
        ([4], 4, 0),
        ([4], 2, -1),
        ([-9, -4, 0, 6], -4, 1),
    ],
)
def test_binary_search(values, key, expected):
    original = values.copy()
    assert binary_search(values, key) == expected
    assert values == original


# test for W1-5 by_day()
def test_by_day_courseExampleResults():
    items = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]
    assert by_day(items) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }


def test_by_day_emptyListResults():
    assert by_day([]) == {}


def test_by_day_singleCourseResults():
    assert by_day([("CSC10014", "Mon")]) == {
        "Mon": ["CSC10014"],
    }


def test_by_day_unsortedCoursesResults():
    items = [
        ("Physics", "Wed"),
        ("Algorithms", "Wed"),
        ("Calculus", "Wed"),
        ("Biology", "Wed"),
    ]
    assert by_day(items) == {
        "Wed": ["Algorithms", "Biology", "Calculus", "Physics"],
    }


def test_by_day_multipleDaysResults():
    items = [
        ("Physics", "Wed"),
        ("Calculus", "Mon"),
        ("Algorithms", "Fri"),
        ("Biology", "Mon"),
        ("Databases", "Fri"),
    ]
    assert by_day(items) == {
        "Wed": ["Physics"],
        "Mon": ["Biology", "Calculus"],
        "Fri": ["Algorithms", "Databases"],
    }


def test_by_day_sameCourseOnDifferentDaysResults():
    items = [
        ("Programming", "Mon"),
        ("Programming", "Fri"),
    ]
    assert by_day(items) == {
        "Mon": ["Programming"],
        "Fri": ["Programming"],
    }
