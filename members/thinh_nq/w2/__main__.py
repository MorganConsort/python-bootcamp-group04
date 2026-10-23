import argparse
import sys
from pathlib import Path

from .io_utils import load_tasks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "csv",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[3] / "samples/tasks.csv",
    )
    args = parser.parse_args()
    try:
        tasks = load_tasks(args.csv)
    except (OSError, ValueError) as exc:
        print(f"Cannot load {args.csv}: {exc}", file=sys.stderr)
        return 1
    for task in tasks:
        print(
            f"{task.title}: importance {task.importance}, {task.effort_h:g} h, due {task.deadline.isoformat()}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
