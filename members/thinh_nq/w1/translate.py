"""W1-4: Translate C++ to Python – Matrix transpose.

Difference from C++:
In C++, you would typically use nested vectors and manual index loops
to build the transposed matrix. In Python, list comprehensions provide
a concise and readable alternative.
"""


def transpose(matrix):
    """Return the transpose of a 2D matrix (list of lists)."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


# Keep the original insertion_sort for reference
def insertion_sort(a):
    """Sort a list of integers in-place using insertion sort and return it."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
