"""Public API for checking administrator/root privileges."""

from ._core import is_admin, is_admin_user

__all__ = ["is_admin", "is_admin_user"]
