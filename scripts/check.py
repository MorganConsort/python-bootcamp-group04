"""Run Ruff and the instructor tests for one member and week, like CI does.

Usage (from the repository root):
    python scripts/check.py --member dat_vt --week 3
    python scripts/check.py --member thinh_nq --week 1 --variant 3
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> int:
    """Print and run a command from the repository root; return its exit code."""
    print("$", " ".join(cmd), flush=True)
    return subprocess.run(cmd, cwd=ROOT, check=False).returncode


def main(argv: list[str] | None = None) -> int:
    """Lint the member's week folder, then run that week's instructor tests."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--member", required=True, help="folder under members/, e.g. dat_vt")
    parser.add_argument("--week", required=True, type=int, help="week number, e.g. 3")
    parser.add_argument("--variant", default="1", help="W1 variant (only used for week 1)")
    args = parser.parse_args(argv)

    folder = ROOT / "members" / args.member / f"w{args.week}"
    if not folder.is_dir():
        print(f"error: {folder.relative_to(ROOT)} does not exist", file=sys.stderr)
        return 1

    tests = [sys.executable, "-m", "pytest", "-q", f"tests/test_w{args.week}.py",
             "--member", args.member]
    if args.week == 1:
        tests += ["--variant", args.variant]

    lint = run([sys.executable, "-m", "ruff", "check", str(folder.relative_to(ROOT))])
    result = run(tests)
    print("\nRuff:", "passed" if lint == 0 else "FAILED")
    print("Tests:", "passed" if result == 0 else "FAILED")
    return 0 if lint == 0 and result == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
