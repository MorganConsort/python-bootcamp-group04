# Week 2 homework design

Approved scope: Minh (`minh_vg`) individual W2-1 through W2-5, shared T-W2,
CI fixes, separate submission notes, and repair of Minh's existing Week 1 regression.
User clarification: read the existing README for context; do not edit it.
Other members' individual implementations and instructor `tests/` stay untouched.
The user explicitly declined repairs to other members' CI blockers.

## Approach

Keep Minh's dataclass, CSV/JSON utilities, exception, and runnable package in
`members/minh_vg/w2/`. The alternative of importing all individual exercises
from shared code would hide individual deliverables. Use a separate shared
Task/Block contract and four small planner modules for the team assignment.
The user approved this approach and implementation on 2026-10-23.

## Behavior

- Task validates importance 1-5; effort must be finite and nonnegative.
- CSV uses the exact four-field header, ISO dates, UTF-8 and line-numbered
  ValueErrors. JSON serializes deadlines to ISO strings.
- `InfeasiblePlan` carries needed_h and available_h; equality is feasible,
  with relative tolerance 1e-12 for floating-point summation (no absolute tolerance).
- `python -m members.minh_vg.w2 [csv]` prints loaded tasks, using the sample
  CSV by default and returning a clear error for invalid or missing files.
- Priority is importance / max(1, days_left), sorted descending with stable ties.
- Greedy allocation follows supplied order, allows a partial last task, and
  never mutates tasks. Zero-effort tasks produce no blocks.
- Render returns a deterministic readable numbered plan; an empty plan says so.

## Team and verification

Interpret the supplied cycle as reviewer -> reviewee:
Dat -> Dang -> Minh -> Thang -> Thinh -> Man -> Dat.
Minh tests Thang's existing `tranquyetthang27` Week 1 implementation.
Six-member split: Dat/Man parse implementation/tests, Dang/Minh priority
implementation/tests, Thang allocation plus tests, Thinh rendering plus tests.
This is a proposed assignment, not evidence of those people's authorship.

Use separate student checks outside instructor `tests/`. CI runs the six actual
Week 1 member/variant combinations, Minh Week 2 instructor checks, and student
tests, without selecting unassigned Week 3. Keep failing checks visible.

Prepare separate PR content for Minh, contract, four modules, and maintenance.
Human authorship, all-six contract reviews, approvals, merge, time spent, and
weekly tag must never be fabricated. GitHub access may block remote submission.
