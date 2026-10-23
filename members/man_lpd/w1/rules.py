def  can_register_thesis(credits: int, gpa: float) -> bool:
    if credits < 120:
        return False
    return not gpa < 2.0

def  missing(credits, gpa) -> list[str]:
    miss = []
    if credits < 120:
        crenum = 120 - credits
        syntax = "more credits" if (crenum > 1) else "more credit"
        miss.append(f"need {crenum} {syntax}")
    if gpa < 2.0:
        gpanum = round(2.0 - gpa, 2)
        miss.append(f"need {gpanum} more GPA points")
    return miss


