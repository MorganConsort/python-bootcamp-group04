def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    schedule: dict[str, list[str]] = {}
    for course, day in items:
        schedule.setdefault(day, []).append(course)

    for day in schedule:
        schedule[day].sort()

    return schedule
