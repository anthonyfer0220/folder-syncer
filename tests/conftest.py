import pytest


@pytest.fixture
def temp_src(tmp_path):
    """
    Set up temporary source directory for testing
    """

    # Create source directory
    src = tmp_path / "source"
    src.mkdir()

    # Add files to source directory
    (src / "foo.txt").write_text("Foo")
    (src / "bar.txt").write_text("Bar")
    (src / "subdir").mkdir()
    (src / "subdir" / "sub.txt").write_text("Sub")

    return src


@pytest.fixture
def temp_dest(tmp_path):
    """
    Set up temporary destination directory for testing
    """

    # Create destination directory
    dest = tmp_path / "destination"
    dest.mkdir()

    return dest


@pytest.fixture
def assert_system_exit():
    """
    Fixture to provide a reusable helper to check that the system properly exits
    """

    def _assert(func):
        # Expect program to terminate with SystemExit
        with pytest.raises(SystemExit) as excinfo:
            func()

        # Verify the exit code is 1, indicating an error
        assert excinfo.value.code == 1, "Should exit with status code 1"

    return _assert