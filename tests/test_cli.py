from __future__ import annotations

from is_admin_user import _cli


def test_cli_prints_true_and_exits_zero_for_admin(monkeypatch, capsys):
    monkeypatch.setattr(_cli, "is_admin_user", lambda: True)

    assert _cli.main([]) == 0
    assert capsys.readouterr().out == "true\n"


def test_cli_prints_false_and_exits_one_for_standard_user(monkeypatch, capsys):
    monkeypatch.setattr(_cli, "is_admin_user", lambda: False)

    assert _cli.main([]) == 1
    assert capsys.readouterr().out == "false\n"


def test_cli_quiet_mode_suppresses_output(monkeypatch, capsys):
    monkeypatch.setattr(_cli, "is_admin_user", lambda: False)

    assert _cli.main(["--quiet"]) == 1
    assert capsys.readouterr().out == ""
