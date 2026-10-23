"""Run with `python -m members.tranquyetthang27.w2` to load and print sample tasks."""

from pathlib import Path

from .io_utils import load_tasks

SAMPLES = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> None:
    tasks = load_tasks(SAMPLES)
    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
