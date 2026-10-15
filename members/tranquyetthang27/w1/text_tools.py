import string


def word_count(text: str) -> dict[str, int]:
    punctuation_to_remove = ".,!?;:"
    cleaned_text = ""
    for char in text:
        if char not in punctuation_to_remove:
            cleaned_text += char
        else:
            cleaned_text += " "
    words = cleaned_text.lower().split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:

    counts = word_count(text)

    element_sorted = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    return element_sorted[:k]
