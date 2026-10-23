# Week 2 submission handoff

## Prepared scope

Minh's W2-1/2/3/5 and W2-4 tests for Thang; shared Task/Block contract;
parse, prioritise, allocate, render and tests; CI repairs and separate notes.
Minh's missing iterative DFS is restored. Instructor tests and other members'
individual code remain unchanged, as explicitly requested.

## PR structure and human actions

| PR | Branch | Base |
|---|---|---|
| [#20 Minh W2](https://github.com/MorganConsort/python-bootcamp-group04/pull/20) | `py/w2-MikaelVo639` | `main` |
| [#21 contract](https://github.com/MorganConsort/python-bootcamp-group04/pull/21) | `py/tw2-contract` | `py/w2-MikaelVo639` |
| [#22 parse](https://github.com/MorganConsort/python-bootcamp-group04/pull/22) | `py/tw2-parse` | `py/tw2-contract` |
| [#23 prioritise](https://github.com/MorganConsort/python-bootcamp-group04/pull/23) | `py/tw2-prioritise` | `py/tw2-parse` |
| [#24 allocate](https://github.com/MorganConsort/python-bootcamp-group04/pull/24) | `py/tw2-allocate` | `py/tw2-prioritise` |
| [#25 render](https://github.com/MorganConsort/python-bootcamp-group04/pull/25) | `py/tw2-render` | `py/tw2-allocate` |
| [#26 CI/README](https://github.com/MorganConsort/python-bootcamp-group04/pull/26) | `py/w2-ci-readme` | `py/tw2-render` |

Tracking issues: [#18 individual](https://github.com/MorganConsort/python-bootcamp-group04/issues/18)
and [#19 team](https://github.com/MorganConsort/python-bootcamp-group04/issues/19).

Keep individual submission, shared contract, and each module in distinct PRs.
Team PRs are stacked so the contract can be reviewed first. Merge from the
bottom upward and retarget each next PR after its base merges. Preparation under
Minh's login is AI-assisted drafting, not evidence of the proposed owners'
contributions. The team leader must confirm the proposed task allocation below.

| Module | Proposed implementation owner | Proposed test owner |
|---|---|---|
| parse | Dat | Man |
| prioritise | Dang | Minh |
| allocate | Thang | Thang |
| render | Thinh | Thinh |

The user clarified that README was context to read, not permission to edit.
The existing root README is preserved exactly. Commands here run from the
repository root, using actual member folders (`minh_vg`, `dat_vt`, `man_lpd`,
`dang_lh`, `thinh_nq`, `tranquyetthang27`).

```text
python -m pip install -r requirements-dev.txt
python -m members.minh_vg.w2
python -m pytest -q tests/test_w2.py --member minh_vg
python -m pytest -q members/minh_vg/w2/tests_for_thang.py student_tests
```

Reviewer -> reviewee: Dat -> Dang -> Minh -> Thang -> Thinh -> Man -> Dat.
Dang reviews Minh's submission. All six review the contract; GitHub does not
allow author approval, so record the author's self-review separately.

## Verification and blockers

Updated after reviewing Thang's full personal W1 task: the expanded peer suite
has **26 passed and 1 failed**, exposing the missing required `sieve(n)` API.
The complete local run now has 91 passed, 1 failed, 11 member-dependent skips,
and 1,543 subtests passed. Do not suppress the failing peer test; Thang must
fix the API in a follow-up PR. See `docs/reviews/2026-10-23-thang-w1.md`.
The earlier initial results below are retained as historical evidence.

Minh's W2 instructor checks and all six W1 instructor runs pass with the
documented API variants. Student tests cover CSV failures, JSON dates,
feasibility, package execution, peer sieve boundaries, prioritisation,
fractional allocation, rendering, and composition. Targeted Ruff is clean.
Bare pytest skips instructor checks without `--member`; explicit runs matter.

Full local student run: 76 tests and 1,543 subtests passed; 11 instructor checks
skip in bare pytest without a selected member. Explicit runs: six W1 runs of
5 tests each pass; Minh W2 run of 3 tests passes. A fresh independent code review
identified fractional budget equality; its regression was verified RED then
GREEN after adding relative tolerance 1e-12 (zero absolute tolerance).

Repository Ruff still fails on Dat's unfinished model, Dat's F541, and Thang's
F401. The user declined edits to those files. Do not suppress the failures.
The latest main CI failure inspected was run 39717316326 at the Ruff step;
pytest was skipped. Remote CI success is not claimed by local execution.

The prepared stack was also checked remotely in
[run 39922391739](https://github.com/MorganConsort/python-bootcamp-group04/actions/runs/39922391739):
all six W1 jobs, Minh W2, and student tests passed. Only lint failed, reporting
exactly the three existing blockers above. This run tested commit `132d861`;
subsequent changes only record evidence and honor the read-only README request.

Five teammates' individual W2 submissions and their peer tests are pending.
Human reviews, approvals, owner confirmation, merge, actual hours, and tag
`py-w2-done` are pending. No student verification is claimed by AI execution.
Older W1 personal assignments differ from generic variants; passing the latter
does not establish completion of every personal W1 assignment.

AI-use disclosure: OpenAI Codex prepared implementation, tests, documentation,
CI changes, and PR drafts. Every student must read and verify their own work;
these drafts do not establish other students' authorship or completed reviews.
