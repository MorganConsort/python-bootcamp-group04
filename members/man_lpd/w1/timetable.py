def by_day(lists : list[tuple[str, str]]) -> dict[str, list[str]]:
    day_dict : dict[str, list[str]] = {}
    for course, day in lists:
        if day not in day_dict:
            day_dict[day] = [course]
        else:
            day_dict[day].append(course)
    
    for courses in day_dict.values():
        courses.sort()

    return day_dict
