"""Group courses by their scheduled day."""


def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Return alphabetically sorted courses per day, preserving duplicates."""
    grouped = {}
    for course, day in items:
        grouped.setdefault(day, []).append(course)
    return {day: sorted(courses) for day, courses in grouped.items()}
