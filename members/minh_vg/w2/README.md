# Minh - Week 2

Section 18.6 exercises W2-1 through W2-5 are implemented in this package.

- Tracking issue: [#18](https://github.com/MorganConsort/python-bootcamp-group04/issues/18).
- Branch: `py/w2-MikaelVo639`; PR title: `py-w2: MikaelVo639`.
- Reviewer: Dang (`hdang-207`). Minh reviews/tests Thang (`tranquyetthang27`).
- W2-4: `tests_for_thang.py` covers Thang's sieve, including negative bounds,
  smallest primes, inclusive bounds, perfect squares, and independent calls.

Run from the repository root:

```text
python -m members.minh_vg.w2
python -m pytest -q tests/test_w2.py --member minh_vg
python -m pytest -q student_tests/test_week2.py members/minh_vg/w2/tests_for_thang.py
python -m ruff check members/minh_vg
```

`Task.days_left(today)` clamps past deadlines to zero. The loader requires the
four-column CSV header and reports physical line numbers for bad records.
JSON writes ISO deadlines. `check_feasible` accepts equal budgets with relative
tolerance 1e-12 for floating-point roundoff and rejects nonfinite/negative
budgets. The package entry point also accepts an optional CSV path.

AI-use disclosure: OpenAI Codex assisted with code, tests, verification, and
submission preparation. Student review, assigned human approval, actual hours,
and repository CI success remain pending. No teammate's authorship is claimed.
