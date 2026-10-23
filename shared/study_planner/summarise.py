"""Summarise an allocated study plan into statistics."""

from shared.contract import Block


def summarise(blocks: list[Block]) -> dict:
    """Return a summary dict with total_hours, task_count, and tasks breakdown.

    Returns:
        {
            "task_count": int,
            "total_hours": float,
            "avg_hours": float,           # 0.0 when empty
            "tasks": [{"title": str, "hours": float}, ...],
        }
    """
    if not blocks:
        return {
            "task_count": 0,
            "total_hours": 0.0,
            "avg_hours": 0.0,
            "tasks": [],
        }

    total = sum(b.hours for b in blocks)
    return {
        "task_count": len(blocks),
        "total_hours": round(total, 2),
        "avg_hours": round(total / len(blocks), 2),
        "tasks": [{"title": b.task.title, "hours": b.hours} for b in blocks],
    }
