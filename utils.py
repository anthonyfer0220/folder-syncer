import os
import shutil
import logging
from pathlib import Path

# Set up path for log files
logs_path = Path(__file__).parent / "logs"

# Create logs folder if it doesn't exist
logs_path.mkdir(exist_ok=True)

#Logging configuration
logging.basicConfig(
    filename=logs_path / "synchronization.log",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.INFO
    )

def sync_folders(src, dest, skipping):
    """
    Synchronize source folder with destination folder

    Copies new or updated files and directories from source to destination
    Delete files and directories in the destination folder that do not exist in the source

    Extra:
    Skip specific files and/or directories from the source folder

    Args:
        src (Path): Source folder
        dest (Path): Destination folder
        skipping (list): List of files and/or directories to skip

    Returns:
        None
    """

    # List all items in source folder
    src_items = os.listdir(src)

    # List all items in destination folder
    dest_items = os.listdir(dest)

    # Iterate through all items in source folder
    for item in src_items:

        # Skip specified files and/or folders
        if item in skipping:
            continue

        src_path = Path(src) / item
        dest_path = Path(dest) / item

        # If the item is a directory
        if src_path.is_dir():
            # If it doesn't exist, copy the directory
            if not dest_path.exists():
                shutil.copytree(src_path, dest_path)
                logging.info(f"Copied directory: {src_path} -> {dest_path}")
            else:
                # Recursively synchronize the directory
                sync_folders(src_path, dest_path, skipping)
        # If the item is a file
        else:
            # Copy file if it doesn't exist or is newer in the source
            if (not dest_path.exists() or
                src_path.stat().st_mtime > dest_path.stat().st_mtime):
                shutil.copy2(src_path, dest_path)
                logging.info(f"Copied file: {src_path} -> {dest_path}")

    # Iterate through items in destination folder
    # and delete those not in source folder
    for item in dest_items:

        src_path = Path(src) / item
        dest_path = Path(dest) / item

        if item in skipping or not src_path.exists():
            delete(dest_path) # Delete file or directory



def delete(dest):
    """
    Delete files or directories with user confirmation

    Informs user of file or directory to be deleted
    Validate user's input
    Performs specific deletion depending on the destination path being a file or a directory

    Args:
        dest (Path): The file or directory to be deleted

    Returns:
        None
    """

    if dest.is_dir():
        item_type = "directory"
    else:
        item_type = "file"

    valid_response = False

    # Validate user's input
    while not valid_response:
        usr_input = input(f"The following {item_type} will be deleted: {dest}\n"
                          f"Do you wish to proceed? (y/n) ")
        if usr_input.lower() == "y": # Perform deletion
            try:
                if item_type == "directory":
                    shutil.rmtree(dest)
                elif item_type == "file":
                    dest.unlink()
                logging.info(f"Deleted {item_type}: {dest}")
            except Exception as e:
                logging.error(f"Failed to delete {item_type}: {dest}. Error: {e}")
            valid_response = True
        elif usr_input.lower() == "n":  # Skip deletion
            break
        else:
            print("Please enter a valid response.")