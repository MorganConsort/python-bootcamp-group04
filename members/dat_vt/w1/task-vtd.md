# Week 1 Task: Vo Dat

| Field | Value |
|---|---|
| Member | Vo Dat (roster member 5) |
| GitHub username | `MorganConsort` |
| Folder | `python-bootcamp/members/dat_vt/w1/` |
| Branch | `py/w1-MorganConsort` |
| Pull request title | `py-w1: MorganConsort` |
| Personal W1-4 task | **Greatest Common Divisor (Euclid's algorithm)** |

Topics to study: variables and types, `if`/`for`/`while`, functions and default arguments, lists, tuples, dicts, sets, strings and f-strings, slicing, comprehensions, `input()`/`print()`. Suggested reading: the official Python tutorial, sections 3 to 5.

All files below go in `python-bootcamp/members/dat_vt/w1/`. Do not edit another member's folder or the instructor tests in `python-bootcamp/tests/`.

## Deliverables checklist

- [ ] `grades.py` (W1-1)
- [ ] `text_tools.py` (W1-2)
- [ ] `rules.py` (W1-3)
- [ ] `translate.py` (W1-4, Greatest Common Divisor (Euclid's algorithm))
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

**Your function: Greatest Common Divisor (Euclid's algorithm).**

Keep the same behavior as the C++ version, write it the Pythonic way, and add a docstring explaining at least one difference from the C++ version.

Write:

```python
def gcd(a: int, b: int) -> int: ...
```

Input: two integers. Output: their greatest common divisor, as a non-negative integer.

Requirements:

- Implement Euclid's algorithm yourself. Do not call `math.gcd`.
- `gcd(a, 0) == abs(a)` and `gcd(0, 0) == 0`.
- Negative inputs are allowed and the result is never negative.
- Optional: in a `if __name__ == "__main__":` block, read two numbers with `input()` and print the result.

```python
>>> gcd(48, 18)
6
>>> gcd(-12, 18)
6
>>> gcd(7, 0)
7
```

C++ starting point:

```cpp
int gcd(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
```

Hints on differences to discuss in your docstring: Python's `%` takes the sign of the divisor while C++'s takes the sign of the dividend, Python integers do not overflow, and Python can swap with `a, b = b, a % b`.

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
   git switch -c py/w1-MorganConsort
   ```
3. **Commit** one exercise at a time (at least five meaningful commits):
   ```text
   feat(py-w1): W1-1 grade summary
   feat(py-w1): W1-2 word counter
   feat(py-w1): W1-3 thesis eligibility
   feat(py-w1): W1-4 translate gcd
   feat(py-w1): W1-5 group timetable by day
   ```
4. **Push** regularly: `git push -u origin py/w1-MorganConsort`
5. **Test** from the repository root:
   ```powershell
   pytest -q python-bootcamp/tests/test_w1.py `
     --member dat_vt `
     --variant <variant>
   ruff check python-bootcamp
   ```
   `--member` must exactly match your folder name (`dat_vt`). Use the `--variant` value that the instructor's tests expect for your translation task.
6. **Pull request:** title `py-w1: MorganConsort`. In the description explain what you completed, add `Closes #<issue-number>`, paste your local pytest and Ruff results, and request your rotation reviewer.
7. **Merge** only after CI is green and the reviewer has approved.
8. **Review** your assigned teammate's PR: right folder, all five exercises present, specs followed, edge cases handled, tests and CI pass, no changes to other folders or tests.
9. **Update `PROGRESS.md`** with your issue number, PR number, reviewer, test result, and actual hours.

## Done when

- [ ] W1 issue created and linked from the PR
- [ ] W1-1 to W1-5 complete in `members/dat_vt/w1/`
- [ ] At least five meaningful commits pushed
- [ ] PR `py-w1: MorganConsort` merged, approved by the rotation reviewer
- [ ] Ruff and pytest pass in CI
- [ ] Teammate PR reviewed
- [ ] `PROGRESS.md` row complete
- [ ] AI assistance disclosed according to the course policy, and all code verified by you
