"""W1-5: Group timetable by day."""


def by_day(items):
    """Group courses by day and sort them alphabetically within each day."""
    result = {}
    for course, day in items:
        result.setdefault(day, []).append(course)
    for day in result:
        result[day].sort()
    return result


# Keep the original function name as an alias
def sorted_list_of_courses(tabletime):
    """Alias for by_day, kept for backward compatibility."""
    return by_day(tabletime)
