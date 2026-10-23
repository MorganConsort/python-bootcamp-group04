"""Run task loader demo: python -m members.dang_lh.w2."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    sample_csv = Path(__file__).resolve().parents[2] / "samples" / "tasks.csv"
    if not sample_csv.exists():
        # Fallback if samples is relative to repository root
        sample_csv = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    tasks = load_tasks(sample_csv)
    for task in tasks:
        print(f"Task: {task.title}, importance: {task.importance}, effort: {task.effort_h}h, deadline: {task.deadline}")


if __name__ == "__main__":
    main()
