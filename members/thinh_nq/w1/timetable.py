def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    schedule: dict[str, list[str]] = {}
    for course, day in items:
        schedule.setdefault(day, []).append(course)

    for day, courses in schedule.items():
        courses.sort()

    return schedule
