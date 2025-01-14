from folder_syncer.utils import sync_folders

def test_copying_new_files(temp_src, temp_dest):
    """
    Test copying new files from source to destination
    """

    print(f"Copying {temp_src.name} -> {temp_dest.name}")

    # Run sync function
    sync_folders(temp_src, temp_dest, skipping=[])

    # Verify files are copied correctly
    assert (temp_dest / "foo.txt").exists(), "foo.txt file should exist in destination"
    assert (temp_dest / "foo.txt").read_text() == "Foo", "foo.txt content should match"
    assert (temp_dest / "bar.txt").exists(), "bar.txt file should exist in destination"
    assert (temp_dest / "bar.txt").read_text() == "Bar", "bar.txt content should match"
    assert (temp_dest / "subdir").exists(), "subdir directory should exist in destination"
    assert (temp_dest / "subdir" / "sub.txt").exists(), "sub.txt file should exist in destination"
    assert (temp_dest / "subdir" / "sub.txt").read_text() == "Sub", "sub.txt content should match"


def test_deleting_files_in_dest(temp_src, temp_dest, monkeypatch):
    """
    Test deleting files in destination that do not exist in source
    """

    # Add file to destination directory
    (temp_dest / "extra.txt").write_text("Extra")
    print(f"Deleting \"extra.txt\" from destination")

    # Mock user input for confirmation
    monkeypatch.setattr("builtins.input", lambda _: "y")

    # Run sync function
    sync_folders(temp_src, temp_dest, skipping=[])

    # Verify extra file is deleted
    assert not (temp_dest / "extra.txt").exists(), "extra.txt file should be removed from destination"


def test_updating_files_in_dest(temp_src, temp_dest):
    """
    Test updating files in destination that are newer in source
    """

    # Update file in source
    (temp_src / "foo.txt").write_text("New Foo")
    print(f"Updating \"foo.txt\"")

    # Run sync function
    sync_folders(temp_src, temp_dest, skipping=[])

    # Verify destination file is updated
    assert (temp_dest / "foo.txt").read_text() == "New Foo", "foo.txt content should match"


def test_excluding_files(temp_src, temp_dest):
    """
    Test excluding files and directories from source to destination during sync
    """

    print(f"Excluding \"foo.txt\" and \"subdir\"")

    # Run sync function with exclusion
    sync_folders(temp_src, temp_dest, skipping=["foo.txt", "subdir"])

    # Verify excluded file and directory are not copied
    assert not (temp_dest / "foo.txt").exists(), "foo.txt file should not exist in destination"
    assert not (temp_dest / "subdir").exists(), "subdir directory should not exist in destination"

    # Verify other file is copied correctly
    assert (temp_dest / "bar.txt").exists(), "bar.txt file should exist in destination"
    assert (temp_dest / "bar.txt").read_text() == "Bar", "bar.txt content should match"
