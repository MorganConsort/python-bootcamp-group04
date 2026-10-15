# Week 1 Task: Vo Gia Minh

| Field | Value |
|---|---|
| Member | Vo Gia Minh (roster member 6) |
| GitHub username | `MikaelVo639` |
| Folder | `python-bootcamp/members/minh_vg/w1/` |
| Branch | `py/w1-MikaelVo639` |
| Pull request title | `py-w1: MikaelVo639` |
| Personal W1-4 task | **Graph representation and Depth First Search** |

Topics to study: variables and types, `if`/`for`/`while`, functions and default arguments, lists, tuples, dicts, sets, strings and f-strings, slicing, comprehensions, `input()`/`print()`. Suggested reading: the official Python tutorial, sections 3 to 5.

All files below go in `python-bootcamp/members/minh_vg/w1/`. Do not edit another member's folder or the instructor tests in `python-bootcamp/tests/`.

## Deliverables checklist

- [x] `grades.py` (W1-1)
- [x] `text_tools.py` (W1-2)
- [x] `rules.py` (W1-3)
- [x] `translate.py` (W1-4, Graph representation and Depth First Search)
- [x] `timetable.py` (W1-5)

---

## W1-1: Grade summary

File: `grades.py`

Write `summary(scores: list[float]) -> dict` returning `{"min", "max", "mean", "median"}`. Round the mean and median to 2 decimals. An empty list raises `ValueError`.

```python
>>> summary([7.5, 9, 6, 8])
{'min': 6, 'max': 9, 'mean': 7.62, 'median': 7.75}
```

## W1-2: Word counter

File: `text_tools.py`

Write:

```python
def word_count(text: str) -> dict[str, int]: ...
def top_k(text: str, k: int) -> list[tuple[str, int]]: ...
```

- Convert words to lowercase and ignore the punctuation characters `. , ! ? ; :`.
- `top_k` sorts by descending count, then alphabetically.

```python
>>> top_k("Git is fun. Git is fast!", 2)
[('git', 2), ('is', 2)]
```

## W1-3: Thesis eligibility

File: `rules.py`

Write:

```python
def can_register_thesis(credits: int, gpa: float) -> bool: ...
def missing(credits: int, gpa: float) -> list[str]: ...
```

- `can_register_thesis` is true when `credits >= 120` and `gpa >= 2.0`.
- `missing` returns clear, human-readable reasons, for example `["need 2 more credits"]`. It returns an empty list when nothing is missing.

## W1-4: Translate C++ to Python (personal variant)

File: `translate.py`

**Your function: Graph representation and Depth First Search.**

Keep the same behavior as the C++ version, write it the Pythonic way, and add a docstring explaining at least one difference from the C++ version.

Write:

```python
def build_graph(edges: list[tuple[int, int]], directed: bool = False,
                nodes: list[int] | None = None) -> dict[int, list[int]]: ...

def dfs(graph: dict[int, list[int]], start: int) -> list[int]: ...

def dfs_iterative(graph: dict[int, list[int]], start: int) -> list[int]: ...
```

Requirements:

- `build_graph` returns an adjacency list as a dict mapping each node to a list of neighbors. Neighbor lists are sorted ascending and contain no duplicates. Edges are added in both directions unless `directed=True`. Nodes listed in `nodes` that have no edges still appear with an empty list.
- `dfs` returns the nodes in the order they are first visited, starting at `start`, using recursion and a `set` for visited nodes. Visit neighbors in ascending order.
- `dfs_iterative` uses an explicit stack and must return exactly the same order as `dfs`.
- Both functions raise `ValueError` if `start` is not in the graph.
- Only nodes reachable from `start` are returned.

```python
>>> g = build_graph([(0, 1), (0, 2), (1, 3), (2, 3)])
>>> g
{0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
>>> dfs(g, 0)
[0, 1, 3, 2]
>>> dfs_iterative(g, 0)
[0, 1, 3, 2]
```

C++ starting point:

```cpp
std::vector<std::vector<int>> build_graph(int n, const std::vector<std::pair<int,int>>& edges) {
    std::vector<std::vector<int>> adj(n);
    for (auto [u, v] : edges) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (auto& nb : adj) std::sort(nb.begin(), nb.end());
    return adj;
}

void dfs(const std::vector<std::vector<int>>& adj, int u,
         std::vector<bool>& visited, std::vector<int>& order) {
    visited[u] = true;
    order.push_back(u);
    for (int v : adj[u])
        if (!visited[v]) dfs(adj, v, visited, order);
}
```

Hints on differences to discuss in your docstring: C++ uses a `vector<vector<int>>` indexed by node number while Python uses a `dict` of lists (nodes need not be `0..n-1`), a `set` replaces `vector<bool>`, the C++ version fills an output parameter while Python returns the order, and Python's default recursion limit (about 1000) makes deep graphs a reason to also write the iterative version.

## W1-5: Group the timetable

File: `timetable.py`

Given a list of `(course, day)` tuples, return a dict from day to an alphabetically sorted list of courses. Use a comprehension or `dict.setdefault`.

```python
def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]: ...
```

```python
>>> by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")])
{'Mon': ['CSC10001', 'CSC10014'], 'Tue': ['MTH00003']}
```

---

## Workflow

1. **Issue:** create one W1 issue. Assign it to yourself, add labels `python-hw` and `w1`, milestone `PY-W1`, name your rotation reviewer, add a checkbox for each of W1-1 to W1-5, and record estimated and actual hours.
2. **Branch:**
   ```powershell
   git switch main
   git pull
   git switch -c py/w1-MikaelVo639
   ```
3. **Commit** one exercise at a time (at least five meaningful commits):
   ```text
   feat(py-w1): W1-1 grade summary
   feat(py-w1): W1-2 word counter
   feat(py-w1): W1-3 thesis eligibility
   feat(py-w1): W1-4 translate graph representation and DFS
   feat(py-w1): W1-5 group timetable by day
   ```
4. **Push** regularly: `git push -u origin py/w1-MikaelVo639`
5. **Test** from the repository root:
   ```powershell
   pytest -q python-bootcamp/tests/test_w1.py `
     --member minh_vg `
     --variant <variant>
   ruff check python-bootcamp
   ```
   `--member` must exactly match your folder name (`minh_vg`). Use the `--variant` value that the instructor's tests expect for your translation task.
6. **Pull request:** title `py-w1: MikaelVo639`. In the description explain what you completed, add `Closes #<issue-number>`, paste your local pytest and Ruff results, and request your rotation reviewer.
7. **Merge** only after CI is green and the reviewer has approved.
8. **Review** your assigned teammate's PR: right folder, all five exercises present, specs followed, edge cases handled, tests and CI pass, no changes to other folders or tests.
9. **Update `PROGRESS.md`** with your issue number, PR number, reviewer, test result, and actual hours.

## Done when

- [x] W1 issue created: [issue #4](https://github.com/MorganConsort/python-bootcamp-group04/issues/4); replacement submission tracked in `PROGRESS.md`
- [x] W1-1 to W1-5 complete in `members/minh_vg/w1/`
- [x] At least five meaningful commits pushed
- [ ] PR `py-w1: MikaelVo639` merged, approved by the rotation reviewer
- [ ] Ruff and pytest pass in CI
- [ ] Teammate PR reviewed
- [ ] `PROGRESS.md` row complete
- [ ] AI assistance disclosed according to the course policy, and all code verified by you

## Implementation notes

All five coding exercises are implemented. The graph and DFS assignment above
is the personal W1-4 specification; the README's generic variant table differs.

Student tests are in `test_exercises.py`; no instructor tests were provided in
this checkout. Run from the repository root with Python 3.10 or newer:

```powershell
python -m unittest discover -s members/minh_vg/w1 -p test_exercises.py -v
python -m pytest -q members/minh_vg/w1/test_exercises.py
ruff check members/minh_vg/w1
```

AI-use disclosure: OpenAI Codex assisted with implementation and local test
creation and execution. Personal review and verification by Vo Gia Minh are
still pending, so the combined disclosure/verification checkbox remains open.
Submission evidence is tracked in the root `PROGRESS.md`. The accidental
unreviewed merge of PR #5 was undone by revert PR #6. The replacement submission
uses `codex/w1-MikaelVo639-review` and awaits teammate review. Keep it open until
the required approval and CI conditions are met; local verification does not
count as approval or CI. The original five exercise commits remain in history.
