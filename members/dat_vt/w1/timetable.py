course_days = [("Math", "Monday"), ("History", "Wednesday"), ("Physics", "Monday"), ("Art", "Wednesday")]

result = {}
# 1. Group the courses by day
for course, day in course_days:
    result.setdefault(day, []).append(course)

# 2. Sort the course lists alphabetically
for day in result:
    result[day].sort()

print(result)
# Output: {'Monday': ['Math', 'Physics'], 'Wednesday': ['Art', 'History']}
