"""Summarize a nonempty collection of grades."""


def summary(scores: list[float]) -> dict:
    """Return the minimum, maximum, mean, and median without changing scores."""
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    count = len(ordered)
    median = (ordered[(count - 1) // 2] + ordered[count // 2]) / 2
    return {
        "min": ordered[0],
        "max": ordered[-1],
        "mean": round(sum(ordered) / count, 2),
        "median": round(median, 2),
    }
