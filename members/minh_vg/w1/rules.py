"""Check the credit and GPA requirements for thesis registration."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether both thesis registration requirements are met."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Explain each unmet registration requirement in credit-then-GPA order."""
    reasons = []
    if credits < 120:
        remaining = 120 - credits
        unit = "credit" if remaining == 1 else "credits"
        reasons.append(f"need {remaining} more {unit}")
    if gpa < 2.0:
        reasons.append("need a GPA of at least 2.0")
    return reasons
