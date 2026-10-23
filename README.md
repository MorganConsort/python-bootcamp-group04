# Python Bootcamp: Evaluator Guide

**Course:** CSC10014 team project, Computational Thinking lab
**Repository:** [`MorganConsort/python-bootcamp-group04`](https://github.com/MorganConsort/python-bootcamp-group04)
**Audience:** the professor, TA, or any evaluator grading this repository

This README is a preview for the person grading the work. It tells you who is on the team, where each piece of evidence lives, what a complete submission looks like, and how to check it quickly. Student setup and exercise instructions are in the bootcamp's own materials and are intentionally not repeated here.

## 1. At a glance

| Question | Answer |
|---|---|
| What is being graded? | Eight weeks of individual Python exercises, plus shared team work in later weeks |
| Where is the evidence? | Only in this GitHub repository: issues, branches, commits, pull requests (PRs), reviews, CI results, tags, and `PROGRESS.md` |
| What is the graded version? | The weekly tag `py-wN-done` (for example `py-w1-done`), pushed by Member 1 after all PRs are merged |
| How many members? | 6 (see the roster below) |
| What is *not* graded? | Anything sent by email or chat, or work that exists only on a student's computer |

## 2. Team roster

| Member | GitHub username | Folder name | Roster number | Individual folder |
|:-:|---|---|:-:|---|
| 1 | [`MorganConsort`](https://github.com/MorganConsort)  | `dat_vt` | 1 |`members/dat_vt/` |
| 2 | [`LePhanDucMan-pa`](https://github.com/LePhanDucMan-pa) | `man_lpd` | 2 | `members/man_lpd/` |
| 3 | [`thinh-nguyen-007`](https://github.com/thinh-nguyen-007) | `thinh_nq` | 3 | `members/thinh_nq/` |
| 4 | [`tranquyetthang27`](https://github.com/tranquyetthang27) | `tranquyetthang27` | 4 | `members/tranquyetthang27/` |
| 5 | [`hdang-207`](https://github.com/hdang-207) |  `dang_lh` | 5 |  `members/dang_lh/` |
| 6 | [`MikaelVo639`](https://github.com/MikaelVo639) | `minh_vg` | 6 | `members/minh_vg/` |

**Roster notes**

- Member 1 is responsible for pushing every weekly `py-wN-done` tag.
- Member 1 is also the owner of the repository account, so some repository-level activity (settings, branch protection) may appear under `MorganConsort`. Do not read this as extra individual work.

### Identifiers to expect in the history

| Member | Weekly branch | PR title | Commit prefix |
|:-:|---|---|---|
| 1 | `py/wN-MorganConsort` | `py-wN: MorganConsort` | `feat(py-wN): ...` |
| 2 | `py/wN-LePhanDucMan-pa` | `py-wN: LePhanDucMan-pa` | `feat(py-wN): ...` |
| 3 | `py/wN-thinh-nguyen-007` | `py-wN: thinh-nguyen-007` | `feat(py-wN): ...` |
| 4 | `py/wN-tranquyetthang27` | `py-wN: tranquyetthang27` | `feat(py-wN): ...` |
| 5 | `py/wN-hdang-207` | `py-wN: hdang-207` | `feat(py-wN): ...` |
| 6 | `py/wN-MikaelVo639` | `py-wN: MikaelVo639` | `feat(py-wN): ...` |

Replace `N` with the week number. Later team weeks may use a topic suffix such as `py/w6-<username>-<topic>`.

### Current Week 2 homework (Section 18.6, pages 61-62)

The arrow means **reviewer -> reviewee**:
**Dat -> Dang -> Minh -> Thang -> Thinh -> Man -> Dat**.

| Reviewer | GitHub | Reviews | Reviewed by |
|---|---|---|---|
| Dat | MorganConsort | Dang | Man |
| Dang | hdang-207 | Minh | Dat |
| Minh | MikaelVo639 | Thang | Dang |
| Thang | tranquyetthang27 | Thinh | Minh |
| Thinh | thinh-nguyen-007 | Man | Thang |
| Man | LePhanDucMan-pa | Dat | Thinh |

Each member completes W2-1 `models.py`, W2-2 `io_utils.py`, W2-3 `errors.py`,
W2-4 `tests_for_<reviewee>.py` (at least five pytest tests, including an extra
edge case), and W2-5 `__init__.py`/`__main__.py` in their own `w2/` package.
Minh's tests target Thang's W1-4 sieve in `members/tranquyetthang27/w1/`.
The older `members/thang_qt/` folder is only a task placeholder.

Minh's package runs from the root with Python 3.12 or newer:

```text
python -m members.minh_vg.w2
python -m members.minh_vg.w2 samples/tasks.csv
python -m pytest -q tests/test_w2.py --member minh_vg
python -m pytest -q members/minh_vg/w2/tests_for_thang.py student_tests
```

The CSV header is `title,importance,effort_h,deadline`. Dates use `YYYY-MM-DD`,
importance is 1-5, and effort is finite and nonnegative. Invalid rows report
their line number. JSON uses ISO date strings.

**T-W2:** all six members must review the PR adding `shared/contract.py` before
module PRs merge. The author records a self-review because GitHub does not
permit the author to approve their own PR. Each module needs its own PR/tests.
Proposed six-member allocation for the team leader to confirm:

| Module / function | Implementation owner | Test owner |
|---|---|---|
| `parse.py`: `parse_csv(path)` | Dat | Man |
| `prioritise.py`: `prioritise(tasks, today)` | Dang | Minh |
| `allocate.py`: `allocate(tasks, hours)` | Thang | Thang |
| `render.py`: `render(blocks)` | Thinh | Thinh |

Shared code is prepared as AI-assisted draft work under Minh's account; this
table does not establish the named members' authorship. Owners must review and
verify their task PRs. Priority uses importance divided by `max(1, days_left)`
with stable ties. Greedy allocation preserves supplied order and allows a
partial final task without mutating tasks. Empty plans render an explicit
message. A shared CLI is T-W3 and is outside this assignment.

CI runs lint, all six actual W1 member/variant combinations, Minh W2, and student
tests in separate jobs. Other members add W2 CI jobs as their packages arrive.
Instructor tests stay unchanged. Current **repository-wide lint blockers** are
Dat's unfinished W2 model (line 17), Dat's W1 `rules.py` F541 (line 16), and
Thang's W1 `text_tools.py` F401 (line 1). Their code remains untouched at the
user's explicit request; do not suppress these checks or merge failing PRs.
See [submission handoff](docs/week2-submission.md) and `PROGRESS.md` for status.

## 3. Repository map for the evaluator

```text
python-bootcamp/
|-- README.md          This guide
|-- PROGRESS.md        Self-reported row per member per week: issue, PR, reviewer, tests, hours
|-- members/
|   `-- <folder>/w1 ... w8/   Each member's individual work (one folder per member)
|-- shared/            Team code (contract.py, study_planner/) used in the team weeks
`-- tests/             Instructor tests and fixtures (students must not edit these)
```

| Open this | To learn |
|---|---|
| `PROGRESS.md` | What each member claims, with issue and PR numbers and reported hours |
| `members/<folder>/wN/` | The actual code for that member and week |
| `shared/` | Team deliverables and who touched them |
| `tests/` | The ground truth for correctness (compare against the git history to detect tampering) |
| Pull requests tab | Reviews, comments, CI status, and merge order |
| Tags | The graded snapshot for each week |

For Week 1, each member folder should contain five files: `grades.py`, `text_tools.py`, `rules.py`, `translate.py`, and `timetable.py`. Later weeks follow the same pattern, one folder per week, with file names given by the instructor's tests.

`translate.py` has generic instructor-test APIs below. Personal task files also assign Dat GCD, Man binary search, Thinh insertion sort, Thang sieve, Dang merge sort, and Minh graph/DFS. Passing an instructor variant alone does not certify those personal tasks:

| Variant | Expected translation in `translate.py` |
|:-:|---|
| 1 | Binary search |
| 2 | In-place insertion sort |
| 3 | Matrix transpose |
| 4 | Sieve of Eratosthenes |

## 4. What a complete weekly submission looks like

Each member should leave this trail on GitHub. If a link in the chain is missing, the work is incomplete or was not done through the required process.

1. **Issue:** one per member per week, assigned to the member, labeled `python-hw` and `wN`, in milestone `PY-WN`, with exercise checkboxes, a named reviewer, and estimated and actual hours.
2. **Branch:** named `py/wN-<github-username>`, created from an up-to-date `main`.
3. **Commits:** at least five meaningful commits, roughly one per exercise, in Conventional Commit style, pushed over time (not all at once).
4. **Pull request:** titled `py-wN: <github-username>`, containing `Closes #<issue>`, local pytest and Ruff results, and the assigned reviewer requested.
5. **Review:** approved by the assigned rotation reviewer after real review comments, with CI green before merge.
6. **Merge:** merged into `main`, never committed directly to `main`.
7. **Progress row:** the member's row in `PROGRESS.md` is complete with issue, PR, reviewer, test result, and actual hours.
8. **Tag:** Member 1 pushes `py-wN-done` after all members have merged.
9. **Teammate review given:** each member also reviewed their assigned teammate's PR (check the reviews tab, not just the approval).

## 5. How to grade (about 10 minutes per member per week)

1. **Check out the graded version, not the tip of `main`.**
   ```bash
   git fetch --all --tags
   git checkout py-w1-done
   ```
2. **Open `PROGRESS.md`** and note each member's claimed issue, PR, reviewer, and hours.
3. **Open each member's PR** from those numbers. Confirm the title, `Closes #`, the pytest and Ruff results, the assigned reviewer, CI green, and merged status.
4. **Read the review thread.** Look for comments that show the reviewer understood the code, not an immediate "LGTM".
5. **Inspect the member folder.** All required files are present, are in the correct folder, and the right variant was implemented.
6. **Re-run the tests** yourself (commands in section 8).
7. **Scan the commit history** for count, spacing, message quality, and correct author identity.
8. **Check integrity** (no edits to instructor tests, no changes to other members' folders, no secrets).
9. **Fill in the scoring sheet** in section 7.

### Grading criteria

Weights are for the instructor to decide. Each row is a pass/fail or scaled check.

| Area | What to verify | Where to look |
|---|---|---|
| Correctness | Instructor tests pass for the member's folder and variant | Local pytest run, CI result |
| Code quality | Readable, decomposed into clear functions, handles edge cases, meets stated complexity or style requirements, Ruff clean | Source files, `ruff check` |
| Process | Issue, branch, PR, and Conventional Commit messages all follow the required pattern | Issues, PRs, `git log` |
| Commit history | At least five meaningful commits, spread over time | `git log`, `git shortlog` |
| Review given | The member reviewed the assigned teammate with substantive comments | Reviews tab |
| Review received | The assigned reviewer approved, and CI was green before merge | PR page |
| Integrity | No weakened tests, no work in another member's folder, no secrets or generated files | Diff and file listing |
| Documentation | `PROGRESS.md` complete, reflection and AI-use disclosure present where required | `PROGRESS.md`, PR description |
| Team delivery | Weekly tag pushed on time, `main` protected, every member visible | Tags, PR history |

## 6. Lateness and partial credit

- The deadline for homework is 23:59 on the day before the next session, unless the instructor announces otherwise.
- A PR counts as submitted only when it is **merged into `main`, CI is green, and the assigned reviewer approved it**.
- Commits made after the weekly tag stay visible in the history. Grade them only if your late policy allows.
- A draft PR opened on time with a note about what is missing can earn partial credit. Nothing pushed earns none.

## 7. Scoring sheets

### Individual sheet (one block per week)

Copy one block per week, or print and fill by hand. Tick, score, or write the number or link as appropriate.

**Week: ____ Tag: `py-w__-done` Graded on: ________**

| Member | Issue # | PR # | Reviewer (actual) | Reviewer correct? | Merged and CI green? | Files present | Variant correct | Tests pass | Ruff clean | ≥ 5 commits | Review given | `PROGRESS.md` row | Integrity OK | Score | Notes |
|:-:|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|---|
| 1 `MorganConsort` | | | | | | | | | | | | | | | |
| 2 `LePhanDucMan-pa` | | | | | | | | | | | | | | | |
| 3 `thinh-nguyen-007` | | | | | | | | | | | | | | | |
| 4 `tranquyetthang27` | | | | | | | | | | | | | | | |
| 5 `hdang-207` | | | | | | | | | | | | | | | |
| 6 `MikaelVo639` | | | | | | | | | | | | | | | |

### Team sheet

| Item | Evidence | Pass / Score | Notes |
|---|---|---|---|
| All members submitted a PR that week | PR list | | |
| Weekly tag pushed by Member 1 | Tags page | | |
| Tag points to the commit after the last merge | `git log` at tag | | |
| `main` protected, no direct commits | `git log --first-parent main` | | |
| CI passing on `main` at the tag | Actions tab | | |
| Reviews distributed according to the rotation | Reviews tab | | |
| Every member visible in PRs or reviews | PR and review history | | |
| Shared code merged through reviewed PRs (team weeks) | `shared/` history | | |

### Contribution factor

The team score can be adjusted per person by a contribution factor. Evidence to consider:

| Source | What it tells you |
|---|---|
| `git shortlog -sne --no-merges` | Commits per person |
| Merged PR list per author | Authored work |
| Reviews per reviewer | Review participation |
| `PROGRESS.md` hours | Self-reported effort |
| Timing of commits and reviews | Steady work versus last-minute pushes |

Commit counts alone are a weak signal. Compare them with PRs, reviews, and the actual content of the changes.

## 8. Command cheat sheet

Run from the repository root.

**Re-run the tests for one member**

```bash
pytest -q tests/test_w1.py --member dang_lh --variant 1
pytest -q tests/test_w1.py --member man_lpd --variant 1
pytest -q tests/test_w1.py --member thinh_nq --variant 3
pytest -q tests/test_w1.py --member tranquyetthang27 --variant 4
pytest -q tests/test_w1.py --member dat_vt --variant 1
pytest -q tests/test_w1.py --member minh_vg --variant 2
ruff check .
```

Use these variant values for the actual instructor APIs, not roster numbers. Personal W1-4 tasks also require their own tests. Run Week 2 explicitly with `python -m pytest -q tests/test_w2.py --member minh_vg`. Bare pytest skips instructor checks without `--member`.

**Setup for the evaluator (once)**

```bash
git clone git@github.com:MorganConsort/python-bootcamp-group04.git
cd python-bootcamp-group04
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

**Pull requests and reviews**

```bash
gh pr list --state merged --limit 100 --json number,title,author,mergedAt,reviews
gh pr view <number> --json reviews,statusCheckRollup,files
gh pr diff <number> --name-only      # did the PR touch another member's folder?
```

**Commit history at the graded tag**

```bash
git log --oneline --no-merges py-w1-done
git log --format="%h %an <%ae> %ad %s" --date=iso py-w1-done
git shortlog -sne --no-merges py-w1-done
git log --first-parent --format="%h %an %s" main     # direct commits to main show up without a PR merge
```

**Instructor tests untouched**

```bash
git log --oneline -- tests
git diff <previous_tag> py-w1-done -- tests
```

**Secrets and generated files**

```bash
git grep -I -n -i -E "(api[_-]?key|secret|password|token)" py-w1-done
git ls-tree -r --name-only py-w1-done | grep -E "(^|/)(\.venv|__pycache__|\.env$)"
```

## 9. Red flags

| Observation | Why it matters |
|---|---|
| All commits created within a few minutes of each other | Work may have been pasted in at the end rather than built up |
| Approval with no comments, or approved within seconds | Review may not have been real |
| Approved by someone other than the assigned reviewer, or self-approved | Breaks the review rotation |
| Edits to `tests/` that remove, skip, or loosen a check | Instructor tests may have been weakened to pass |
| Changes inside another member's folder | Violates the individual-work rule |
| Code that does not match the member's variant | Wrong variant implemented, or code copied from another member |
| Two members with near-identical solutions | Possible copying; compare history and authorship |
| Very polished code with no AI-use disclosure | The course requires AI assistance to be disclosed |
| Merge with failing CI | Violates the merge rule |
| `.env`, `.venv/`, `__pycache__/`, or keys in the repository | Secrets or generated files committed |
| Commits under an unlinked or unknown email | Contribution cannot be attributed (check `.mailmap`) |

## 10. Common false alarms

| What you might see | Likely explanation |
|---|---|
| Folder aliases differ in older task files | Use the actual folders listed in the roster, particularly `thinh_nq` and `tranquyetthang27` |
| A folder name does not obviously match the GitHub username | Folder names are chosen by the team (for example `dat_vt` for `MorganConsort`). Use the roster above |
| Instructor variants differ from personal assignments | Variants select an API, not a roster position. Dang also has merge sort and Minh also has graph/DFS; test those separately |
| `PROGRESS.md` is updated in a separate small PR | Allowed. It may be submitted with the homework PR or as a follow-up |
| Repository settings changes by one account | The repository owner configures branch protection and CI |
| Pytest cannot find the member | The command was not run from the repository root, or `--member` does not exactly match the folder |
