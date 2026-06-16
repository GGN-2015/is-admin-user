# is-admin-user

Check whether the current Python process is running as an administrator.

`is-admin-user` is a tiny, dependency-free Python package that works across
Windows, Linux, and macOS. It exposes a programmable function interface for
checking whether the current process has administrative privileges.

## Installation

```bash
pip install is-admin-user
```

For local development:

```bash
pip install -e .
```

## Usage

```python
from is_admin_user import is_admin_user

if is_admin_user():
    print("Running as administrator/root")
else:
    print("Running as a standard user")
```

You can also use the shorter alias:

```python
from is_admin_user import is_admin

if is_admin():
    print("Administrative privileges are available")
```

## Platform behavior

- Windows: returns `True` when the current process token is running with
  administrator privileges.
- Linux: returns `True` when the effective user ID is `0` (`root`).
- macOS: returns `True` when the effective user ID is `0` (`root`).

On Windows, an account that belongs to the Administrators group may still return
`False` if the Python process was not started with elevated privileges.

## API

### `is_admin_user() -> bool`

Returns `True` when the current Python process has administrator/root
privileges, otherwise returns `False`.

### `is_admin() -> bool`

Alias for `is_admin_user()`.

## Development

Run the test suite with:

```bash
python -m pytest
```
