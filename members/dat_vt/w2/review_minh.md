# W2-4 Code Review: dat_vt → minh_vg (W1)

**Reviewer:** dat_vt ([@MorganConsort](https://github.com/MorganConsort))  
**Reviewee:** minh_vg ([@MikaelVo639](https://github.com/MikaelVo639))  
**Date:** 2026-10-23  
**Test file:** [`members/dat_vt/w2/tests_for_minh.py`](../w2/tests_for_minh.py)

---

## Summary

I reviewed all five W1 modules (`grades`, `rules`, `text_tools`, `timetable`, `translate`) and wrote **10 pytest tests** covering both standard scenarios and edge cases not present in the instructor tests.

## Test Results

| # | Test | Module | Status |
|---|------|--------|--------|
| 1 | `test_grades_all_identical_scores` | grades | ✅ PASSED |
| 2 | `test_grades_two_scores_median` | grades | ✅ PASSED |
| 3 | `test_rules_exactly_at_boundary` | rules | ✅ PASSED |
| 4 | `test_rules_just_below_both` | rules | ✅ PASSED |
| 5 | `test_top_k_negative_k` | text_tools | ✅ PASSED |
| 6 | `test_word_count_multiline_tabs` | text_tools | ✅ PASSED |
| 7 | `test_timetable_single_day_multiple_courses` | timetable | ✅ PASSED |
| 8 | `test_insertion_sort_already_sorted` | translate | ✅ PASSED |
| 9 | `test_insertion_sort_single_element` | translate | ✅ PASSED |
| 10 | `test_dfs_single_node_graph` | translate | ✅ PASSED |

**Result: 10/10 passed ✅**

## Edge Cases Not Covered by Instructor Tests

- **`test_grades_all_identical_scores`** – All scores identical (min = max = mean = median). Verifies the median calculation doesn't break when there's zero variance.
- **`test_top_k_negative_k`** – Negative `k` argument. Instructor tests only check `k=0`; this confirms negative values also return `[]`.
- **`test_dfs_single_node_graph`** – Graph with a single isolated node and no edges. Tests both recursive and iterative DFS on the trivial graph.

## Code Quality Notes

Overall, minh_vg's W1 code is clean and well-structured:
- Good use of docstrings across all modules
- `grades.summary()` correctly preserves the input list
- `text_tools` uses `str.maketrans` — concise and efficient
- `rules.missing()` handles singular/plural for credits (`"credit"` vs `"credits"`) — nice touch
- `timetable.by_day()` uses a dict comprehension for the final sort — clean one-liner
- `translate.py` includes both recursive and iterative DFS with proper `ValueError` on missing start node

No failing tests or bugs found. 👍

---

> **@MikaelVo639** — Please review the tests above and respond if anything looks incorrect or if you have questions.
