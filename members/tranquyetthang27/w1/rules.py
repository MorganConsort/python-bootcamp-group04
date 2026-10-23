def can_register_thesis(credits: int, gpa: float) -> bool:
    return bool(credits >= 120 and gpa >= 2.0)


def missing(credits, gpa) -> list[str]:
    reasons = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append(f"need to improve at least {2.0 - gpa} for graduation")
    return reasons
