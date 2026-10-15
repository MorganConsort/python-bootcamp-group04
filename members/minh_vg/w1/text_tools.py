"""Count words and rank them by frequency."""


def word_count(text: str) -> dict[str, int]:
    """Count lowercase, whitespace-separated words, ignoring . , ! ? ; :."""
    cleaned = text.lower().translate(str.maketrans("", "", ".,!?;:"))
    counts = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return up to k words by descending count, breaking ties alphabetically."""
    if k <= 0:
        return []
    ranked = sorted(word_count(text).items(), key=lambda item: (-item[1], item[0]))
    return ranked[:k]
