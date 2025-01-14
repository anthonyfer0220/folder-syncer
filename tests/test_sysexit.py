from main import main
from tests.conftest import assert_system_exit


def test_less_than_required_arguments(temp_src, monkeypatch, assert_system_exit):
    """
    Test passing less than 3 arguments
    """

    print(f"Fewer than 3 arguments passed")

    # Simulate fewer than 3 arguments passed
    monkeypatch.setattr("main.sys.argv", ["main.py", f"{temp_src}"])

    # Assert SystemExit
    assert_system_exit(main)

def test_source_not_exist(temp_src, temp_dest, monkeypatch, assert_system_exit):
    """
    Test when source directory does not exist
    """

    # Simulate passing a non-existent source directory
    monkeypatch.setattr("main.sys.argv", ["main.py", f"{temp_src}/not_an_existing_dir", f"{temp_dest}"])

    # Assert SystemExit
    assert_system_exit(main)


def test_dest_not_dir(temp_src, temp_dest, monkeypatch, assert_system_exit):
    """
    Test when destination exists but is not a directory
    """

    # Create a destination as a file instead of a directory
    (temp_dest / "dest_not_a_dir").touch()

    # Simulate passing a destination as a file
    monkeypatch.setattr("main.sys.argv", ["main.py", f"{temp_src}", f"{temp_dest}/dest_not_a_dir"])

    # Assert SystemExit
    assert_system_exit(main)


def test_source_and_dest_same(temp_src, monkeypatch, assert_system_exit):
    """
    Test when source and destination directories are the same
    """

    # Simulate passing the same path for source and destination
    monkeypatch.setattr("main.sys.argv", ["main.py", f"{temp_src}", f"{temp_src}"])

    # Assert SystemExit
    assert_system_exit(main)