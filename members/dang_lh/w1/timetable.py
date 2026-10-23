"""W1-5: Group timetable by day.

Organizes course items by weekday and sorts course codes alphabetically.
"""


def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort them alphabetically.

    Args:
        items: List of (course_code, day) tuples.

    Returns:
        Dict mapping each day to an alphabetically sorted list of courses.
    """
    schedule: dict[str, list[str]] = {}
    for course, day in items:
        schedule.setdefault(day, []).append(course)

    # Sort course codes alphabetically for each day
    for day, courses in schedule.items():
        courses.sort()

    return schedule
