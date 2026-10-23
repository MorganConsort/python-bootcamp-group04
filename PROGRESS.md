# Python bootcamp progress

## Current Week 2 preparation (2026-10-23)

Latest follow-up: original PRs #20-26 are merged, but #21-26 targeted feature
branches, so shared code and revised CI are still absent from main `7fa8fa2`.
A follow-up branch `py/w2-followup-MikaelVo639` carries the surviving full stack
to [PR #27 targeting main](https://github.com/MorganConsort/python-bootcamp-group04/pull/27).
All five non-author members are requested as reviewers. The AI-assisted
author-side contract check is [recorded on #21](https://github.com/MorganConsort/python-bootcamp-group04/pull/21#pullrequestreview-5626563088);
it is not student verification or approval.
Minh's C413/I001 lint findings are fixed; isolated Ruff
for his folder passes. See `docs/repo-audit-2026-10-23.md` and the AI-assisted
contract check in `docs/reviews/2026-10-23-contract-check.md`.
Older rows below record preparation-time review requests, not current PR state.

| Member / task | Status | Reviewer / action |
|---|---|---|
| Minh (`minh_vg`) W2-1/2/3/5 | Implemented and locally tested | Dang (`hdang-207`); human review pending |
| Minh W2-4 | Expanded tests: 26 passed, 1 failed because Thang lacks required `sieve(n)` API | Minh -> Thang; follow-up fix needed |
| Thinh (`thinh_nq`) W2-1/2/3/5 | Implemented and locally tested | Thang (`tranquyetthang27`) |
| Thinh W2-4 | Peer tests for binary search: 21 passed | Thinh -> Man |
| Shared contract | Prepared with tests | All six must review; no approvals claimed |
| Four shared modules | Prepared with tests and pipeline check | Owner allocation proposed in docs/week2-submission.md; confirmation pending |
| Other members' individual W2 | Not completed by this change | Each owner supplies their own work |

| Submission | Issue | PR | Assigned human review | Local result |
|---|---|---|---|---|
| Minh W2 | [#18](https://github.com/MorganConsort/python-bootcamp-group04/issues/18) | [#20](https://github.com/MorganConsort/python-bootcamp-group04/pull/20) | Dang (`hdang-207`), requested | W2 instructor: 3 passed; peer tests now expose missing Thang API (26 passed, 1 failed) |
| Thinh W2 | [#39](https://github.com/MorganConsort/python-bootcamp-group04/issues/39) | [#40](https://github.com/MorganConsort/python-bootcamp-group04/pull/40) | Thang (`tranquyetthang27`), requested | W2 instructor: 3 passed; peer tests: 21 passed |
| Shared contract | [#19](https://github.com/MorganConsort/python-bootcamp-group04/issues/19) | [#21](https://github.com/MorganConsort/python-bootcamp-group04/pull/21) | All five non-author members requested; author's self-review pending | Contract tests passed |
| Parse | #19 | [#22](https://github.com/MorganConsort/python-bootcamp-group04/pull/22) | Man requested; proposed owner Dat | Parser tests passed |
| Prioritise | #19 | [#23](https://github.com/MorganConsort/python-bootcamp-group04/pull/23) | Dang requested; proposed test owner Minh | Priority tests passed |
| Allocate | #19 | [#24](https://github.com/MorganConsort/python-bootcamp-group04/pull/24) | Thang requested | Allocation tests passed |
| Render | #19 | [#25](https://github.com/MorganConsort/python-bootcamp-group04/pull/25) | Thinh requested | Rendering tests passed |
| CI / separate docs | #18, #19 | [#26](https://github.com/MorganConsort/python-bootcamp-group04/pull/26) | Dat requested | Expanded full run: 91 passed, 1 peer API test failed, 1,543 subtests passed; six W1 runs: 5 passed each |

Follow-up Thang review: [posted on PR #8](https://github.com/MorganConsort/python-bootcamp-group04/pull/8#pullrequestreview-5625695435),
with report in `docs/reviews/2026-10-23-thang-w1.md`. The new failing
test enforces `sieve(n)` from Thang's personal task; generic instructor tests
only exercise `primes_up_to(n)`. Thang's code and all README files remain
unchanged. Earlier all-green student results predate the expanded API check.

Full cycle (reviewer -> reviewee): Dat -> Dang -> Minh -> Thang -> Thinh -> Man -> Dat.
Local execution is not evidence of human review, remote CI success, merge, or
student hours. Estimated and actual hours were not supplied.

AI-use disclosure: OpenAI Codex prepared Minh's Week 2 work, shared drafts,
tests, CI configuration, documentation, and submission preparation. No other
member's authorship or personal verification is claimed.

Repository lint remains blocked by Dat's incomplete W2 model/F541 and Thang's
unused import/F401. Their files were left untouched at the user's request.
Instructor `tests/` were not modified. See `docs/week2-submission.md`.

## Historical Week 1 reports

The reports below describe earlier submissions; references to absent tests/CI
and reviewer preferences are historical. The review cycle above applies now.

| Week | Member | Issue | PR | Reviewer | Local verification | Estimated hours | Actual hours |
|---|---|---|---|---|---|---|---|
| 1 | MikaelVo639 (`minh_vg`) | [#4](https://github.com/MorganConsort/python-bootcamp-group04/issues/4) | [#5](https://github.com/MorganConsort/python-bootcamp-group04/pull/5) | Not requested, per author | pytest: 31 tests and 1,543 subtests passed; Ruff lint and Python formatting passed | Not supplied | Not supplied |
| 1 | thinh-nguyen-007 (`thinh_nq`) | [#9](https://github.com/MorganConsort/python-bootcamp-group04/issues/9) | [#10](https://github.com/MorganConsort/python-bootcamp-group04/pull/10) | Team review | Local unit tests pass (all 5 modules verified); clean code | 2h | 2h |
| 1 | hdang-207 (`dang_lh`) | [#13](https://github.com/MorganConsort/python-bootcamp-group04/issues/13) | [#14](https://github.com/MorganConsort/python-bootcamp-group04/pull/14) | MorganConsort | Manual and smoke tests passed (all 5 modules verified); clean code | 2h | 2h |
| 1 | LePhanDucMan-pa (`man_lpd`) | [#2](https://github.com/MorganConsort/python-bootcamp-group04/issues/2) | [#3](https://github.com/MorganConsort/python-bootcamp-group04/pull/3) | MorganConsort | Binary-search examples passed locally; no instructor tests or CI workflow present | 4h | 4h |

The implementation follows `members/minh_vg/w1/task-vgm.md`, including graph
representation and DFS for W1-4. No instructor tests or CI workflow were present
in the checkout. Local checks do not establish CI, approval, or merge status.

AI-use disclosure: OpenAI Codex assisted with implementation, test creation,
local verification, and GitHub submission preparation. Personal verification by
Vo Gia Minh and self-reported effort hours are not claimed.

Nguyen Quoc Thinh implemented in-place insertion sort for W1-4 following
`members/thinh_nq/w1/task-nqt.md`. All 5 modules verified with unit tests.
AI-use disclosure: Antigravity assisted with scaffolding and test verification.
All code and logic verified by Nguyen Quoc Thinh.

Le Hong Dang implemented recursive merge sort for W1-4 following
`members/dang_lh/w1/task-lhd.md`. All 5 modules verified locally.
AI-use disclosure: Antigravity assisted with scaffolding and edge-case review.
All code and logic verified by Le Hong Dang.

Le Phan Duc Man implemented binary search for W1-4 following
`members/man_lpd/task-lpdm.md`. Binary-search examples were verified locally.
No instructor tests or CI workflow were present in the repository.

AI-use disclosure: AI assistance was used for Git and GitHub workflow guidance.
All submitted code was reviewed and verified by Le Phan Duc Man.
