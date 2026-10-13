"""W1-3: Thesis eligibility rules.

Checks if a student meets graduation thesis eligibility requirements.
"""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True if the student meets thesis requirements (credits >= 120 and gpa >= 2.0)."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return human-readable reasons if any requirement is not met."""
    reasons: list[str] = []
    if credits < 120:
        needed_credits = 120 - credits
        if needed_credits == 1:
            reasons.append("need 1 more credit")
        else:
            reasons.append(f"need {needed_credits} more credits")

    if gpa < 2.0:
        needed_gpa = round(2.0 - gpa, 2)
        reasons.append(f"need {needed_gpa:.2f} more GPA" if needed_gpa != int(needed_gpa) else f"need {needed_gpa} more GPA")

    return reasons
