"""W2-4: Dat reviews Minh's W1 functions.

At least five tests, including edge cases the instructor tests do not cover.
"""

import pytest

from members.minh_vg.w1 import grades, rules, text_tools, timetable, translate


# ── grades ──────────────────────────────────────────────────────────────────

def test_grades_all_identical_scores():
    """Edge case: all scores the same – min, max, mean, median all equal."""
    result = grades.summary([5.0, 5.0, 5.0])
    assert result == {"min": 5.0, "max": 5.0, "mean": 5.0, "median": 5.0}


def test_grades_two_scores_median():
    """Two scores – median is the average of both."""
    result = grades.summary([3.0, 7.0])
    assert result["median"] == 5.0


# ── rules ───────────────────────────────────────────────────────────────────

def test_rules_exactly_at_boundary():
    """Boundary: exactly 120 credits and 2.0 GPA should pass."""
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.missing(120, 2.0) == []


def test_rules_just_below_both():
    """Just under both thresholds should give two reasons."""
    assert rules.can_register_thesis(119, 1.99) is False
    reasons = rules.missing(119, 1.99)
    assert len(reasons) == 2


# ── text_tools ──────────────────────────────────────────────────────────────

def test_top_k_negative_k():
    """Edge case not in instructor tests: negative k should return []."""
    assert text_tools.top_k("hello world hello", -5) == []


def test_word_count_multiline_tabs():
    """Mixed whitespace: tabs and newlines should split correctly."""
    result = text_tools.word_count("a\tb\nc\ta")
    assert result == {"a": 2, "b": 1, "c": 1}


# ── timetable ───────────────────────────────────────────────────────────────

def test_timetable_single_day_multiple_courses():
    """All courses on the same day should be sorted alphabetically."""
    items = [("Zeal", "Mon"), ("Apple", "Mon"), ("Mango", "Mon")]
    result = timetable.by_day(items)
    assert result == {"Mon": ["Apple", "Mango", "Zeal"]}


# ── translate (insertion sort) ──────────────────────────────────────────────

def test_insertion_sort_already_sorted():
    """Edge case: already-sorted input should remain unchanged."""
    assert translate.insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_insertion_sort_single_element():
    """Single-element list is trivially sorted."""
    assert translate.insertion_sort([42]) == [42]


def test_dfs_single_node_graph():
    """Edge case: graph with a single node and no edges."""
    graph = translate.build_graph([], nodes=[0])
    assert translate.dfs(graph, 0) == [0]
    assert translate.dfs_iterative(graph, 0) == [0]
