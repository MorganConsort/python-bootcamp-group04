def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores must not be empty")

    n = len(scores)
    min_val = min(scores)
    max_val = max(scores)
    mean_val = round(sum(scores) / n, 2)

    sorted_scores = sorted(scores)
    if n % 2 == 1:
        median_val = sorted_scores[n // 2]
    else:
        median_val = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": round(median_val, 2),
    }
