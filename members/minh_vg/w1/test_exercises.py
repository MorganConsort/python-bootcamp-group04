"""Student checks for the five exercises; instructor tests are separate."""

import unittest
from itertools import product

from grades import summary
from rules import can_register_thesis, missing
from text_tools import top_k, word_count
from timetable import by_day
from translate import build_graph, dfs, dfs_iterative


class GradeTests(unittest.TestCase):
    def test_assignment_example(self):
        self.assertEqual(
            summary([7.5, 9, 6, 8]),
            {"min": 6, "max": 9, "mean": 7.62, "median": 7.75},
        )

    def test_empty_scores(self):
        with self.assertRaises(ValueError):
            summary([])

    def test_single_score(self):
        self.assertEqual(
            summary([8.125]),
            {"min": 8.125, "max": 8.125, "mean": 8.12, "median": 8.12},
        )

    def test_odd_count_and_rounding(self):
        self.assertEqual(
            summary([9, 1, 2]),
            {"min": 1, "max": 9, "mean": 4.0, "median": 2.0},
        )
        self.assertEqual(summary([1, 2, 2])["mean"], 1.67)

    def test_even_median_uses_middle_scores(self):
        self.assertEqual(summary([10, 0, 8, 4])["median"], 6.0)

    def test_input_is_unchanged(self):
        scores = [9, 6, 8]
        summary(scores)
        self.assertEqual(scores, [9, 6, 8])


class WordTests(unittest.TestCase):
    def test_assignment_example(self):
        self.assertEqual(top_k("Git is fun. Git is fast!", 2), [("git", 2), ("is", 2)])

    def test_case_punctuation_and_whitespace(self):
        self.assertEqual(
            word_count("Git, GIT. git!\nPython? python;\tPYTHON:"),
            {"git": 3, "python": 3},
        )

    def test_empty_and_punctuation_only(self):
        for text in ("", " \n\t ", ". , ! ? ; :"):
            with self.subTest(text=text):
                self.assertEqual(word_count(text), {})
                self.assertEqual(top_k(text, 3), [])

    def test_other_characters_are_preserved(self):
        self.assertEqual(word_count("It's well-known"), {"it's": 1, "well-known": 1})

    def test_frequency_then_alphabetical_order(self):
        self.assertEqual(
            top_k("z b a z b c", 10),
            [("b", 2), ("z", 2), ("a", 1), ("c", 1)],
        )

    def test_nonpositive_k(self):
        self.assertEqual(top_k("one two", 0), [])
        self.assertEqual(top_k("one two", -1), [])


class RuleTests(unittest.TestCase):
    def test_both_thresholds_are_inclusive(self):
        self.assertTrue(can_register_thesis(120, 2.0))
        self.assertTrue(can_register_thesis(150, 4.0))
        self.assertEqual(missing(120, 2.0), [])

    def test_credits_missing(self):
        self.assertFalse(can_register_thesis(118, 3.0))
        self.assertEqual(missing(118, 3.0), ["need 2 more credits"])

    def test_one_credit_uses_singular(self):
        self.assertEqual(missing(119, 2.0), ["need 1 more credit"])

    def test_gpa_missing(self):
        self.assertFalse(can_register_thesis(120, 1.99))
        self.assertEqual(missing(120, 1.99), ["need a GPA of at least 2.0"])

    def test_both_requirements_missing(self):
        self.assertFalse(can_register_thesis(0, 0.0))
        self.assertEqual(
            missing(0, 0.0),
            ["need 120 more credits", "need a GPA of at least 2.0"],
        )


class GraphTests(unittest.TestCase):
    def assert_traversals(self, graph, start, expected):
        self.assertEqual(dfs(graph, start), expected)
        self.assertEqual(dfs_iterative(graph, start), expected)

    def test_assignment_example(self):
        graph = build_graph([(0, 1), (0, 2), (1, 3), (2, 3)])
        self.assertEqual(graph, {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]})
        self.assert_traversals(graph, 0, [0, 1, 3, 2])

    def test_sorted_unique_neighbors_and_self_loop(self):
        self.assertEqual(
            build_graph([(5, 2), (5, -1), (2, 5), (5, 2), (5, 5)]),
            {5: [-1, 2, 5], 2: [5], -1: [5]},
        )

    def test_directed_edges_include_sink(self):
        graph = build_graph([(10, 20), (10, 20)], directed=True)
        self.assertEqual(graph, {10: [20], 20: []})
        self.assert_traversals(graph, 10, [10, 20])
        self.assert_traversals(graph, 20, [20])

    def test_isolated_nodes_and_empty_graph(self):
        graph = build_graph([], nodes=[42, -10, 42])
        self.assertEqual(graph, {42: [], -10: []})
        self.assertEqual(build_graph([]), {})
        self.assert_traversals(graph, 42, [42])

    def test_disconnected_component_is_excluded(self):
        graph = build_graph([(1, 2), (10, 20)], nodes=[99])
        self.assert_traversals(graph, 1, [1, 2])

    def test_unsorted_neighbors_cycles_and_cross_edges(self):
        graph = {0: [3, 2, 1, 1], 1: [2, 0], 2: [3, 1], 3: [0]}
        self.assert_traversals(graph, 0, [0, 1, 2, 3])
        self.assertEqual(graph[0], [3, 2, 1, 1])

    def test_missing_start(self):
        for graph in ({}, {1: []}):
            for traversal in (dfs, dfs_iterative):
                with (
                    self.subTest(graph=graph, traversal=traversal.__name__),
                    self.assertRaises(ValueError),
                ):
                    traversal(graph, 99)

    def test_calls_have_independent_visited_sets(self):
        graph = build_graph([(1, 2)])
        self.assert_traversals(graph, 1, [1, 2])
        self.assert_traversals(graph, 2, [2, 1])
        self.assert_traversals(graph, 1, [1, 2])

    def test_iterative_matches_recursive_on_all_three_node_graphs(self):
        possible_edges = list(product(range(3), repeat=2))
        for mask in range(1 << len(possible_edges)):
            edges = [
                edge for bit, edge in enumerate(possible_edges) if mask & (1 << bit)
            ]
            graph = build_graph(edges, directed=True, nodes=[0, 1, 2])
            for start in graph:
                with self.subTest(mask=mask, start=start):
                    self.assertEqual(dfs_iterative(graph, start), dfs(graph, start))

    def test_iterative_handles_a_deep_chain(self):
        graph = build_graph([(node, node + 1) for node in range(1999)], directed=True)
        self.assertEqual(dfs_iterative(graph, 0), list(range(2000)))

    def test_builder_does_not_change_inputs(self):
        edges = [(2, 1), (2, 1)]
        nodes = [8, 2]
        build_graph(edges, nodes=nodes)
        self.assertEqual(edges, [(2, 1), (2, 1)])
        self.assertEqual(nodes, [8, 2])


class TimetableTests(unittest.TestCase):
    def test_assignment_example(self):
        self.assertEqual(
            by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]),
            {"Mon": ["CSC10001", "CSC10014"], "Tue": ["MTH00003"]},
        )

    def test_empty_timetable(self):
        self.assertEqual(by_day([]), {})

    def test_duplicates_and_input_are_preserved(self):
        items = [("Z", "Mon"), ("A", "Mon"), ("Z", "Mon")]
        self.assertEqual(by_day(items), {"Mon": ["A", "Z", "Z"]})
        self.assertEqual(items, [("Z", "Mon"), ("A", "Mon"), ("Z", "Mon")])


if __name__ == "__main__":
    unittest.main()
