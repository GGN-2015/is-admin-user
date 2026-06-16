from __future__ import annotations

from is_admin_user import is_admin, is_admin_user
from is_admin_user import _core


class _FakeShell32:
    def __init__(self, result: int) -> None:
        self._result = result

    def IsUserAnAdmin(self) -> int:
        return self._result


class _FailingShell32:
    def IsUserAnAdmin(self) -> int:
        raise OSError("administrator check failed")


class _FakeWindll:
    def __init__(self, result: int) -> None:
        self.shell32 = _FakeShell32(result)


def test_returns_true_for_windows_admin(monkeypatch):
    monkeypatch.setattr(_core.sys, "platform", "win32")
    monkeypatch.setattr(_core.ctypes, "windll", _FakeWindll(1), raising=False)

    assert is_admin_user() is True


def test_returns_false_for_windows_standard_user(monkeypatch):
    monkeypatch.setattr(_core.sys, "platform", "win32")
    monkeypatch.setattr(_core.ctypes, "windll", _FakeWindll(0), raising=False)

    assert is_admin_user() is False


def test_returns_false_when_windows_check_fails(monkeypatch):
    monkeypatch.setattr(_core.sys, "platform", "win32")
    monkeypatch.setattr(
        _core.ctypes,
        "windll",
        type("_FailingWindll", (), {"shell32": _FailingShell32()})(),
        raising=False,
    )

    assert is_admin_user() is False


def test_returns_true_for_posix_root(monkeypatch):
    monkeypatch.setattr(_core.sys, "platform", "linux")
    monkeypatch.setattr(_core.os, "geteuid", lambda: 0, raising=False)

    assert is_admin_user() is True


def test_returns_false_for_posix_standard_user(monkeypatch):
    monkeypatch.setattr(_core.sys, "platform", "darwin")
    monkeypatch.setattr(_core.os, "geteuid", lambda: 501, raising=False)

    assert is_admin_user() is False


def test_posix_falls_back_to_real_user_id(monkeypatch):
    monkeypatch.setattr(_core.sys, "platform", "linux")
    monkeypatch.delattr(_core.os, "geteuid", raising=False)
    monkeypatch.setattr(_core.os, "getuid", lambda: 0, raising=False)

    assert is_admin_user() is True


def test_is_admin_alias(monkeypatch):
    monkeypatch.setattr(_core.sys, "platform", "linux")
    monkeypatch.setattr(_core.os, "geteuid", lambda: 0, raising=False)

    assert is_admin() is True
