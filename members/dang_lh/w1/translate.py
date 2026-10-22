"""W1-4: Translate C++ to Python – Binary search.

Differences from C++ implementation:
1. Python uses // for integer division instead of /.
2. Python integers have arbitrary precision, so no overflow concern with
   (low + high) // 2.
3. Python does not require explicit type declarations.
"""


def binary_search(a, key):
    """Return the index of key in sorted list a, or -1 if not found."""
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Keep the original merge sort for reference
def merge(left, right):
    """Merge two sorted lists into a single sorted list stably."""
    result = []
    i = 0
    j = 0
    left_len = len(left)
    right_len = len(right)

    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(a):
    """Sort a list of integers using recursive merge sort."""
    if len(a) <= 1:
        return list(a)

    mid = len(a) // 2
    left_sorted = merge_sort(a[:mid])
    right_sorted = merge_sort(a[mid:])

    return merge(left_sorted, right_sorted)
