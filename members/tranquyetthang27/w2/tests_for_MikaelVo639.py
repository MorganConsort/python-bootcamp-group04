"""Peer review: tranquyetthang27 reviews MikaelVo639's W1 exercises.

These tests cover all five W1 files in ``members/minh_vg/w1`` and target edge
cases that ``tests/test_w1.py`` does not exercise: even-length medians,
punctuation-heavy word counts, non-positive ``k``, the singular credit message,
in-place sorting, and graph traversal (the instructor's variant-2 check only
looks at ``insertion_sort``).
"""

import pytest

from members.minh_vg.w1 import grades, rules, text_tools, timetable, translate


def test_summary_even_count_uses_both_middle_scores():
    scores = [10, 0, 8, 4]
    assert grades.summary(scores) == {
        "min": 0,
        "max": 10,
        "mean": 5.5,
        "median": 6.0,
    }
    assert scores == [10, 0, 8, 4], "summary must not reorder the caller's list"


def test_summary_single_score_rounds_mean_and_median():
    assert grades.summary([8.125]) == {
        "min": 8.125,
        "max": 8.125,
        "mean": 8.12,
        "median": 8.12,
    }


def test_summary_empty_scores_raise_value_error():
    with pytest.raises(ValueError):
        grades.summary([])


def test_word_count_ignores_case_whitespace_and_punctuation():
    text = "Git, GIT. git!\nPython? python;\tPYTHON:"
    assert text_tools.word_count(text) == {"git": 3, "python": 3}


def test_word_count_keeps_apostrophes_and_hyphens_inside_words():
    assert text_tools.word_count("It's well-known") == {"it's": 1, "well-known": 1}


@pytest.mark.parametrize("k", [0, -1])
def test_top_k_non_positive_k_returns_empty(k):
    assert text_tools.top_k("a b a", k) == []


def test_top_k_breaks_ties_alphabetically():
    assert text_tools.top_k("z b a z b c", 10) == [
        ("b", 2),
        ("z", 2),
        ("a", 1),
        ("c", 1),
    ]


def test_missing_uses_singular_credit_for_one_remaining_credit():
    """Edge case absent from the instructor tests: 119 credits -> 1 credit."""
    assert rules.can_register_thesis(119, 2.0) is False
    assert rules.missing(119, 2.0) == ["need 1 more credit"]


def test_missing_reports_both_requirements_in_order():
    assert rules.missing(0, 0.0) == [
        "need 120 more credits",
        "need a GPA of at least 2.0",
    ]


def test_thesis_thresholds_are_inclusive():
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.missing(120, 2.0) == []


def test_insertion_sort_is_in_place_and_returns_the_same_list():
    values = [5, -1, 5, 0]
    result = translate.insertion_sort(values)
    assert values == [-1, 0, 5, 5]
    assert result is values


def test_insertion_sort_handles_already_sorted_and_empty_lists():
    assert translate.insertion_sort([]) == []
    assert translate.insertion_sort([1, 2, 3]) == [1, 2, 3]


def test_build_graph_sorts_and_deduplicates_undirected_neighbors():
    assert translate.build_graph([(5, 2), (5, -1), (2, 5), (5, 2)]) == {
        5: [-1, 2],
        2: [5],
        -1: [5],
    }


def test_build_graph_directed_keeps_sinks_and_isolated_nodes():
    assert translate.build_graph([(1, 2)], directed=True, nodes=[3]) == {
        3: [],
        1: [2],
        2: [],
    }


def test_dfs_and_dfs_iterative_agree_on_a_cycle():
    graph = translate.build_graph([(0, 1), (0, 2), (1, 3), (2, 3)])
    assert translate.dfs(graph, 0) == [0, 1, 3, 2]
    assert translate.dfs_iterative(graph, 0) == [0, 1, 3, 2]


def test_traversals_only_return_the_connected_component():
    graph = translate.build_graph([(1, 2), (10, 20)])
    assert translate.dfs(graph, 1) == [1, 2]
    assert translate.dfs_iterative(graph, 10) == [10, 20]


@pytest.mark.parametrize("traversal", [translate.dfs, translate.dfs_iterative])
def test_traversals_reject_a_start_node_missing_from_the_graph(traversal):
    with pytest.raises(ValueError):
        traversal({}, 7)
    with pytest.raises(ValueError):
        traversal({1: []}, 7)


def test_timetable_groups_sorts_and_preserves_duplicate_courses():
    items = [("Z", "Mon"), ("A", "Mon"), ("Z", "Mon"), ("B", "Tue")]
    assert timetable.by_day(items) == {"Mon": ["A", "Z", "Z"], "Tue": ["B"]}
    assert items == [("Z", "Mon"), ("A", "Mon"), ("Z", "Mon"), ("B", "Tue")]


def test_timetable_empty_input_returns_empty_dict():
    assert timetable.by_day([]) == {}
