import pytest
from main import main


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


def test_less_than_required_arguments(temp_src, monkeypatch):
    """
    Test passing less than 3 arguments
    """

    print(f"Fewer than 3 arguments passed")

    # Simulate fewer than 3 arguments passed
    monkeypatch.setattr("main.sys.argv", ["main.py", f"{temp_src}"])

    # Expect program to terminate with SystemExit
    with pytest.raises(SystemExit) as excinfo:
        main()

    # Verify the exit code is 1, indicating an error
    assert excinfo.value.code == 1, "Should exit with status code 1 and Print usage instructions"


def test_source_not_exist(temp_src, temp_dest, monkeypatch):
    """
    Test when source directory does not exist
    """

    # Simulate passing a non-existent source directory
    monkeypatch.setattr("main.sys.argv", ["main.py", f"{temp_src}/not_an_existing_dir", f"{temp_dest}"])

    # Expect program to terminate with SystemExit
    with pytest.raises(SystemExit) as excinfo:
        main()

    # Verify the exit code is 1, indicating an error
    assert excinfo.value.code == 1, "Should exit with status code 1"


def test_dest_not_dir(temp_src, temp_dest, monkeypatch):
    """
    Test when destination exists but is not a directory
    """

    # Create a destination as a file instead of a directory
    (temp_dest / "dest_not_a_dir").touch()

    # Simulate passing a destination as a file
    monkeypatch.setattr("main.sys.argv", ["main.py", f"{temp_src}", f"{temp_dest}/dest_not_a_dir"])

    # Expect program to terminate with SystemExit
    with pytest.raises(SystemExit) as excinfo:
        main()

    # Verify the exit code is 1, indicating an error
    assert excinfo.value.code == 1, "Should exit with status code 1"


def test_source_and_dest_same(temp_src, monkeypatch):
    """
    Test when source and destination directories are the same
    """

    # Simulate passing the same path for source and destination
    monkeypatch.setattr("main.sys.argv", ["main.py", f"{temp_src}", f"{temp_src}"])

    # Expect program to terminate with SystemExit
    with pytest.raises(SystemExit) as excinfo:
        main()

    # Verify the exit code is 1, indicating an error
    assert excinfo.value.code == 1, "Should exit with status code 1"
