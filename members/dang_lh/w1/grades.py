"""W1-1: Grade summary.

Provides a summary of student scores: min, max, mean, and median.
"""

def summary(scores: list[float]) -> dict:
    """Compute summary statistics for a list of scores.

    Args:
        scores: A list of numerical scores.

    Returns:
        A dict with 'min', 'max', 'mean', and 'median' rounded to 2 decimals.

    Raises:
        ValueError: If the scores list is empty.
    """
    if not scores:
        raise ValueError("Error: scores list cannnot be empty")

    min_val = min(scores)
    max_val = max(scores)
    mean_val = round(sum(scores) / len(scores), 2)

    sorted_scores = sorted(scores)
    n = len(scores)
    mid = n // 2
    if n % 2 == 1: 
        median_val = sorted_scores[mid]
    else:
        median_val = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2

    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val
    }
