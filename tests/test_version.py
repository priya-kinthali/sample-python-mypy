from python_project_template import __version__


def test_version() -> str:
    assert __version__ is not None
    return 1
