# Week 1 Task: Le Hong Dang

| Field | Value |
|---|---|
| Member | Le Hong Dang (roster member 1) |
| GitHub username | `hdang-207` |
| Folder | `python-bootcamp/members/dang_lh/w1/` |
| Branch | `py/w1-hdang-207` |
| Pull request title | `py-w1: hdang-207` |
| Personal W1-4 task | **Merge sort** |

Topics to study: variables and types, `if`/`for`/`while`, functions and default arguments, lists, tuples, dicts, sets, strings and f-strings, slicing, comprehensions, `input()`/`print()`. Suggested reading: the official Python tutorial, sections 3 to 5.

All files below go in `python-bootcamp/members/dang_lh/w1/`. Do not edit another member's folder or the instructor tests in `python-bootcamp/tests/`.

## Deliverables checklist

- [x] `grades.py` (W1-1)
- [x] `text_tools.py` (W1-2)
- [x] `rules.py` (W1-3)
- [x] `translate.py` (W1-4, Merge sort)
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

**Your function: Merge sort.**

Keep the same behavior as the C++ version, write it the Pythonic way, and add a docstring explaining at least one difference from the C++ version.

Write:

```python
def merge_sort(a: list[int]) -> list[int]: ...
```

Return a **new** sorted list and leave the input list unchanged.

Requirements:

- Split the list, sort each half recursively, and merge. Write a helper `merge(left, right)` to make the decomposition visible.
- Do not call `sorted()` or `list.sort()`.
- The sort must be stable: equal elements keep their original order (use `<=` when comparing the heads of the two halves).
- Handle an empty list and a single-element list.

```python
>>> merge_sort([38, 27, 43, 3, 9, 82, 10])
[3, 9, 10, 27, 38, 43, 82]
>>> merge_sort([])
[]
```

C++ starting point:

```cpp
void merge(std::vector<int>& a, int l, int m, int r) {
    std::vector<int> left(a.begin() + l, a.begin() + m + 1);
    std::vector<int> right(a.begin() + m + 1, a.begin() + r + 1);
    size_t i = 0, j = 0;
    int k = l;
    while (i < left.size() && j < right.size())
        a[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];
    while (i < left.size()) a[k++] = left[i++];
    while (j < right.size()) a[k++] = right[j++];
}

void merge_sort(std::vector<int>& a, int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    merge_sort(a, l, m);
    merge_sort(a, m + 1, r);
    merge(a, l, m, r);
}
```

Hints on differences to discuss in your docstring: the C++ version sorts in place using index ranges `[l, r]`, while the Python version can use slices and return a new list, and the C++ `merge` fills the original vector from temporary copies while Python builds and returns a fresh result list.

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
   git switch -c py/w1-hdang-207
   ```
3. **Commit** one exercise at a time (at least five meaningful commits):
   ```text
   feat(py-w1): W1-1 grade summary
   feat(py-w1): W1-2 word counter
   feat(py-w1): W1-3 thesis eligibility
   feat(py-w1): W1-4 translate merge sort
   feat(py-w1): W1-5 group timetable by day
   ```
4. **Push** regularly: `git push -u origin py/w1-hdang-207`
5. **Test** from the repository root:
   ```powershell
   pytest -q python-bootcamp/tests/test_w1.py `
     --member dang_lh `
     --variant <variant>
   ruff check python-bootcamp
   ```
   `--member` must exactly match your folder name (`dang_lh`). Use the `--variant` value that the instructor's tests expect for your translation task.
6. **Pull request:** title `py-w1: hdang-207`. In the description explain what you completed, add `Closes #<issue-number>`, paste your local pytest and Ruff results, and request your rotation reviewer.
7. **Merge** only after CI is green and the reviewer has approved.
8. **Review** your assigned teammate's PR: right folder, all five exercises present, specs followed, edge cases handled, tests and CI pass, no changes to other folders or tests.
9. **Update `PROGRESS.md`** with your issue number, PR number, reviewer, test result, and actual hours.

## Done when

- [x] W1 issue created and linked from the PR
- [x] W1-1 to W1-5 complete in `members/dang_lh/w1/`
- [x] At least five meaningful commits pushed
- [x] PR `py-w1: hdang-207` merged, approved by the rotation reviewer
- [ ] Ruff and pytest pass in CI
- [ ] Teammate PR reviewed
- [x] `PROGRESS.md` row complete
- [x] AI assistance disclosed according to the course policy, and all code verified by you
