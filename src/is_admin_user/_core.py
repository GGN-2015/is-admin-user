"""Cross-platform administrator/root privilege checks."""

from __future__ import annotations

import ctypes
import os
import sys


def is_admin_user() -> bool:
    """Return whether the current Python process has administrator privileges.

    On Windows, this checks the current process token for administrator
    privileges. On Linux and macOS, this checks whether the effective user ID is
    0, which is the root user.
    """
    if sys.platform == "win32":
        return _is_windows_admin()

    return _is_posix_root()


def is_admin() -> bool:
    """Return whether the current Python process has administrator privileges."""
    return is_admin_user()


def _is_windows_admin() -> bool:
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except (AttributeError, OSError, ValueError):
        return False


def _is_posix_root() -> bool:
    geteuid = getattr(os, "geteuid", None)
    if callable(geteuid):
        return geteuid() == 0

    getuid = getattr(os, "getuid", None)
    if callable(getuid):
        return getuid() == 0

    return False
