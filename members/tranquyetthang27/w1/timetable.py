def sorted_list_of_courses(tabletime):
    result = {}
    for course, day in tabletime:
        result.setdefault(day, []).append(course)
    for day in result:
        result[day].sort()

    return result
