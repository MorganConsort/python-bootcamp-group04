# Week 3 plan: standard library and tooling

Milestone: [PY-W3](https://github.com/MorganConsort/python-bootcamp-group04/milestone/3).
Instructor tests: `tests/test_w3.py` (do not edit).

## Individual work (W3-1 to W3-4)

Each member creates `members/<folder>/w3/` with `__init__.py`, `dates.py`, `log_stats.py`
and `cli.py`, on branch `py/w3-<github-username>`.

| Member | Folder | Issue | Reviewed by | Reviews |
|---|---|---|---|---|
| MorganConsort (Dat) | `dat_vt` | #43 | Man | Dang |
| LePhanDucMan-pa (Man) | `man_lpd` | #44 | Thinh | Dat |
| thinh-nguyen-007 (Thinh) | `thinh_nq` | #45 | Thang | Man |
| tranquyetthang27 (Thang) | `tranquyetthang27` | #46 | Minh | Thinh |
| hdang-207 (Dang) | `dang_lh` | #47 | Dat | Minh |
| MikaelVo639 (Minh) | `minh_vg` | #48 | Dang | Thang |

Rotation (reviewer -> reviewee): Dat -> Dang -> Minh -> Thang -> Thinh -> Man -> Dat.

## Team work (T-W3: integrate the study planner)

| Task | Owner | Issue |
|---|---|---|
| 1. `shared/study_planner/__main__.py`: parse_csv -> prioritise -> allocate -> render | Dat | #49 |
| 2. End-to-end test with a sample CSV, in `student_tests/` | Man | #50 |
| 3. Error handling: missing file, empty file, infeasible plan | Thinh | #51 |
| 4. `shared/study_planner/README.md` and a short demo in `docs/` | Thang | #52 |

Dang and Minh have no T-W3 role and are the suggested reviewers for the team PRs.
Order: 1 first, then 2 and 3 build on it; 4 can start any time.

## Checking your work

```bash
python scripts/check.py --member <folder> --week 3
```

This runs Ruff on your `w3` folder and `tests/test_w3.py` for you, the same as CI.
In CI, the `week3` job runs for each member once their `w3` folder exists, and the
`study-planner-cli` job runs `python -m shared.study_planner samples/tasks.csv --hours 2`
once `__main__.py` exists. The end-to-end test runs in the `student-tests` job.

## Starting point for `cli.py`

Only the argument handling is given; the planning logic is yours to write and should
reuse your W2 code.

```python
"""W3-3: print tonight's study plan from a task CSV."""

import argparse
import sys
from datetime import date


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plan tonight's study session.")
    parser.add_argument("csv", help="path to the tasks CSV")
    parser.add_argument("--hours", type=float, required=True, help="hours available")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today(),
                        help="YYYY-MM-DD (default: today)")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    # TODO: load the CSV with your W2 code (missing file -> message on stderr, return 1),
    # choose tasks for args.hours, and print the plan.
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Expected output shape for `--hours 2 --today 2026-10-26` on `samples/tasks.csv`:

```text
Tonight (2.0 h):
 1. Assignment ...... 1.5 h
 2. DS exam ......... 0.5 h
```

## Done when

Four individual PRs are merged, the CLI runs from a fresh clone, the end-to-end test
passes in CI, and Dat pushes the `py-w3-done` tag.
