from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Robot Framework suites one by one and generate per-scenario reports."
    )
    parser.add_argument(
        "--browser",
        default=None,
        help="Optional browser override passed to Robot as BROWSER variable.",
    )
    parser.add_argument(
        "--dryrun",
        action="store_true",
        help="Run Robot in dry-run mode without opening browsers.",
    )
    return parser.parse_args()


def discover_suites(tests_dir: Path) -> list[Path]:
    ordered = []
    role_suite = tests_dir / "role_coverage.robot"
    if role_suite.exists():
        ordered.append(role_suite)
    ordered.extend(sorted(tests_dir.glob("scenario_*.robot")))
    return ordered


def main() -> int:
    args = parse_args()
    project_dir = Path(__file__).resolve().parent
    tests_dir = project_dir / "tests"
    report_root = project_dir / "reports" / "robot"

    suites = discover_suites(tests_dir)
    if not suites:
        print("No Robot scenario suites found.")
        return 1

    shutil.rmtree(report_root, ignore_errors=True)
    report_root.mkdir(parents=True, exist_ok=True)

    combined_rc = 0
    for suite in suites:
        suite_name = suite.stem
        suite_output = report_root / suite_name
        suite_output.mkdir(parents=True, exist_ok=True)

        cmd = [
            sys.executable,
            "-m",
            "robot",
            "--outputdir",
            str(suite_output),
            str(suite),
        ]
        if args.dryrun:
            cmd.insert(3, "--dryrun")
        if args.browser:
            cmd.extend(["--variable", f"BROWSER:{args.browser}"])

        print(f"\n=== Running: {suite_name} ===")
        rc = subprocess.run(cmd, cwd=project_dir).returncode
        combined_rc = max(combined_rc, rc)

    print(f"\nPer-scenario reports generated in: {report_root}")
    return combined_rc


if __name__ == "__main__":
    raise SystemExit(main())
