# Week 1 Task: Nguyen Quoc Thinh

| Field | Value |
|---|---|
| Member | Nguyen Quoc Thinh (roster member 3) |
| GitHub username | `thinh-nguyen-007` |
| Folder | `python-bootcamp/members/thinh-nq/w1/` |
| Branch | `py/w1-thinh-nguyen-007` |
| Pull request title | `py-w1: thinh-nguyen-007` |
| Personal W1-4 task | **Insertion sort (in place, return the sorted list)** |

Topics to study: variables and types, `if`/`for`/`while`, functions and default arguments, lists, tuples, dicts, sets, strings and f-strings, slicing, comprehensions, `input()`/`print()`. Suggested reading: the official Python tutorial, sections 3 to 5.

All files below go in `python-bootcamp/members/thinh-nq/w1/`. Do not edit another member's folder or the instructor tests in `python-bootcamp/tests/`.

## Deliverables checklist

- [ ] `grades.py` (W1-1)
- [ ] `text_tools.py` (W1-2)
- [ ] `rules.py` (W1-3)
- [ ] `translate.py` (W1-4, Insertion sort (in place, return the sorted list))
- [ ] `timetable.py` (W1-5)

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

**Your function: Insertion sort (in place, return the sorted list).**

Keep the same behavior as the C++ version, write it the Pythonic way, and add a docstring explaining at least one difference from the C++ version.

Write:

```python
def insertion_sort(a: list[int]) -> list[int]: ...
```

Sort the list **in place** and return the same list object.

Requirements:

- Implement the shifting loop yourself. Do not call `sorted()` or `list.sort()`.
- Handle an empty list and a single-element list.
- Duplicates must be kept, and equal elements must keep their original order.
- After the call, `result is a` must be true.

```python
>>> insertion_sort([5, 2, 4, 6, 1, 3])
[1, 2, 3, 4, 5, 6]
>>> insertion_sort([])
[]
```

C++ starting point:

```cpp
std::vector<int>& insertion_sort(std::vector<int>& a) {
    for (size_t i = 1; i < a.size(); ++i) {
        int key = a[i];
        int j = (int)i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = key;
    }
    return a;
}
```

Hints on differences to discuss in your docstring: C++ takes the vector by non-const reference while Python passes the list object reference, `size_t` is unsigned in C++ (which is why `j` is a signed `int`), and Python's `range` removes the manual index bookkeeping in the outer loop.

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
   git switch -c py/w1-thinh-nguyen-007
   ```
3. **Commit** one exercise at a time (at least five meaningful commits):
   ```text
   feat(py-w1): W1-1 grade summary
   feat(py-w1): W1-2 word counter
   feat(py-w1): W1-3 thesis eligibility
   feat(py-w1): W1-4 translate insertion sort
   feat(py-w1): W1-5 group timetable by day
   ```
4. **Push** regularly: `git push -u origin py/w1-thinh-nguyen-007`
5. **Test** from the repository root:
   ```powershell
   pytest -q python-bootcamp/tests/test_w1.py `
     --member thinh-nq `
     --variant <variant>
   ruff check python-bootcamp
   ```
   `--member` must exactly match your folder name (`thinh-nq`). Use the `--variant` value that the instructor's tests expect for your translation task.
6. **Pull request:** title `py-w1: thinh-nguyen-007`. In the description explain what you completed, add `Closes #<issue-number>`, paste your local pytest and Ruff results, and request your rotation reviewer.
7. **Merge** only after CI is green and the reviewer has approved.
8. **Review** your assigned teammate's PR: right folder, all five exercises present, specs followed, edge cases handled, tests and CI pass, no changes to other folders or tests.
9. **Update `PROGRESS.md`** with your issue number, PR number, reviewer, test result, and actual hours.

## Done when

- [ ] W1 issue created and linked from the PR
- [ ] W1-1 to W1-5 complete in `members/thinh-nq/w1/`
- [ ] At least five meaningful commits pushed
- [ ] PR `py-w1: thinh-nguyen-007` merged, approved by the rotation reviewer
- [ ] Ruff and pytest pass in CI
- [ ] Teammate PR reviewed
- [ ] `PROGRESS.md` row complete
- [ ] AI assistance disclosed according to the course policy, and all code verified by you
