"""Command-line interface for is-admin-user."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import Optional

from ._core import is_admin_user


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the command-line interface and return a process exit code."""
    parser = argparse.ArgumentParser(
        prog="is-admin-user",
        description="Check whether the current process is running as an administrator or root user.",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="suppress output and use only the exit code",
    )
    args = parser.parse_args(argv)

    has_admin_privileges = is_admin_user()
    if not args.quiet:
        print("true" if has_admin_privileges else "false")

    return 0 if has_admin_privileges else 1
