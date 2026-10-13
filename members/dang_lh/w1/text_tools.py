"""W1-2: Word counter.

Provides word counting and top-k frequent word analysis.
"""

def _clean_and_tokenize(text: str) -> list[str]:
    """Tokenize text into lowercase words, ignoring specific punctuation."""
    # Ignore punctuation characters: . , ! ? ; :
    punct = set(".,!?;:")
    cleaned_chars = [c for c in text if c not in punct]
    cleaned_text = "".join(cleaned_chars).lower()
    return cleaned_text.split()


def word_count(text: str) -> dict[str, int]:
    """Count the occurrences of each word in text."""
    counts: dict[str, int] = {}
    for word in _clean_and_tokenize(text):
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k words sorted by descending count, then alphabetically."""
    counts = word_count(text)
    # Sort by (-count, word) to achieve descending count then alphabetical
    sorted_items = sorted(counts.items(), key = lambda item: (-item[1], item[0]))
    return sorted_items[:k]
