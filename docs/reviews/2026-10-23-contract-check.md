# Author-side contract verification (AI-assisted)

Scope: `shared/contract.py` from PR #21, plus its use by the four planner modules.
This is an automated source/test review prepared for Minh, not personal student
verification or a human approval. GitHub cannot accept author approval.

## Checks

- Task has the agreed title, importance, effort_h, and deadline fields.
- Block contains the original Task object and allocated hours.
- Task rejects importance outside 1-5 and negative/nonfinite effort.
- Parsing returns shared Task objects rather than individual model objects.
- Prioritisation is stable, uses importance / max(1, days_left), and leaves
  the original input order intact.
- Allocation preserves Task identity and input effort, and creates positive
  blocks within a finite nonnegative budget. Rendering consumes those blocks.

`student_tests/test_contract.py`, `test_prioritise.py`, and `test_pipeline.py`
passed (3 tests). All shared/student checks also passed in the complete run.
The complete suite has one unrelated failing peer test: Thang lacks the
required `sieve(n)` API. Repository lint has the three documented Dat/Thang
blockers. These failures remain visible.

## Boundaries

Block does not validate hours at construction: the agreed contract defines its
fields, while allocate validates the budget and emits valid blocks. Direct
callers must respect the annotated types. No new validation policy was added.

Verdict: contract and tested composition match the agreed interfaces. The five
non-author teammates' reviews and Minh's personal verification remain human
tasks; automated execution cannot establish those.
