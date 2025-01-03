import sys
import logging
from pathlib import Path
from utils import sync_folders

# A script to synchronize files between a source and a destination folder.

def main():
    # Validate command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python3 main.py \"path/to/source\" \"path/to/destination\"")
        print("Example: python3 main.py \"~/source_folder\" \"~/destination_folder\"")
        sys.exit(1)

    # Set up paths for source and destination folders
    src = Path(sys.argv[1]).expanduser()
    dest = Path(sys.argv[2]).expanduser()

    # Skip ".DS_Store" by default
    skipping = [".DS_Store"]

    # If "skip" flag is used, add following elements to skipping list
    if len(sys.argv) > 3 and (sys.argv[3] == "-s" or sys.argv[3] == "--skip"):
        skipping.extend(sys.argv[4:])

    # Validate paths and Create destination folder if it doesn't exist
    if not src.exists() or not src.is_dir():
        print(f"Source folder {src} does not exist")
        sys.exit(1)

    if not dest.exists():
        dest.mkdir(exist_ok=True)
    elif not dest.is_dir():
        print(f"Path {dest} already exists but it is not a directory")
        sys.exit(1)

    # Synchronize folders
    sync_folders(src, dest, skipping)
    logging.info("Finished syncing successfully")

    logging.shutdown()
    print("Synchronization completed successfully.")

if __name__ == "__main__":
    main()