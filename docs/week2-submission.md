# Week 2 submission handoff

## Prepared scope

Minh's W2-1/2/3/5 and W2-4 tests for Thang; shared Task/Block contract;
parse, prioritise, allocate, render and tests; CI and README repairs.
Minh's missing iterative DFS is restored. Instructor tests and other members'
individual code remain unchanged, as explicitly requested.

## PR structure and human actions

Keep individual submission, shared contract, and each module in distinct PRs.
Team PRs are stacked so the contract can be reviewed first. Merge from the
bottom upward and retarget each next PR after its base merges. Preparation under
Minh's login is AI-assisted drafting, not evidence of the proposed owners'
contributions. The team leader must confirm README's task allocation.

Reviewer -> reviewee: Dat -> Dang -> Minh -> Thang -> Thinh -> Man -> Dat.
Dang reviews Minh's submission. All six review the contract; GitHub does not
allow author approval, so record the author's self-review separately.

## Verification and blockers

Minh's W2 instructor checks and all six W1 instructor runs pass with the
documented API variants. Student tests cover CSV failures, JSON dates,
feasibility, package execution, peer sieve boundaries, prioritisation,
fractional allocation, rendering, and composition. Targeted Ruff is clean.
Bare pytest skips instructor checks without `--member`; explicit runs matter.

Repository Ruff still fails on Dat's unfinished model, Dat's F541, and Thang's
F401. The user declined edits to those files. Do not suppress the failures.
The latest main CI failure inspected was run 39717316326 at the Ruff step;
pytest was skipped. Remote CI success is not claimed by local execution.

Five teammates' individual W2 submissions and their peer tests are pending.
Human reviews, approvals, owner confirmation, merge, actual hours, and tag
`py-w2-done` are pending. No student verification is claimed by AI execution.
Older W1 personal assignments differ from generic variants; passing the latter
does not establish completion of every personal W1 assignment.

AI-use disclosure: OpenAI Codex prepared implementation, tests, documentation,
CI changes, and PR drafts. Every student must read and verify their own work;
these drafts do not establish other students' authorship or completed reviews.
