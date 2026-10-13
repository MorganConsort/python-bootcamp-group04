"""W1-4: Translate C++ to Python - Merge sort variant.

Differences from C++ implementation:
1. In C++, merge sort operates in-place on a mutable std::vector<int> using
   boundary indices [l, r], and the merge step copies elements back into the
   original vector. In Python, idiomatic code uses slicing to split lists and
   returns a new sorted list, leaving the original input unchanged.
2. The Python merge step dynamically builds and returns a fresh result list
   instead of mutating an existing container by index.
"""


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into a single sorted list stably."""
    result: list[int] = []
    i = 0
    j = 0
    left_len = len(left)
    right_len = len(right)

    # Use <= to ensure stability (preserving original order of equal elements)
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(a: list[int]) -> list[int]:
    """Sort a list of integers using recursive merge sort.

    Returns a new list without modifying the original input list.
    """
    if len(a) <= 1:
        return list(a)

    mid = len(a) // 2
    left_sorted = merge_sort(a[:mid])
    right_sorted = merge_sort(a[mid:])

    return merge(left_sorted, right_sorted)
