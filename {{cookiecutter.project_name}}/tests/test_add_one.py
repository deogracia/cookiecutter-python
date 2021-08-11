"""{{cookiecutter.package_name}} default test.

It can be suppressed or updated
"""
from {{cookiecutter.package_name}} import default


def test_add_one():
    """Default test."""
    assert default.add_one(0) == 1
