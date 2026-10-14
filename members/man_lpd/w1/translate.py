# Binary search on the sorted list 
def binary_search(a: list[int], key: int) -> int:
    """
    returns the index of key in a list, or -1 if not found.
    Difference from C++:
    Unlike C++, Python use // for integer division, not /
    Instead, / returns a float, which is not valid for indexing a list.
    Also, in C++, the formula mid = low + (high - low)/2 is used to avoid integer overflow of low + high.
    In Python, integers can be arbitrarily large, hence no need to worry about overflow.
    """
    low, high = 0, len(a) - 1
    while (low <= high):
        mid = (low + high) // 2
        if (a[mid] == key): 
            return mid
        elif (a[mid] < key): 
            low = mid + 1
        else: 
            high = mid - 1
    return -1