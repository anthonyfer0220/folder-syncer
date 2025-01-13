# Folder Syncer

A lightweight Python-based tool to synchronize files and folders by comparing a source folder with a destination folder, copying new or updated files, and removing outdated ones.

Perfectly suited for backups, file replication, or keeping directories organized.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
  - [Example](#example)
  - [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Install

This project requires [Python 3](https://www.python.org/).

1. Verify Python 3 is installed on your system:
    ```sh
    python3 --version
    ```

   If not, install it using Homebrew:
    ```sh
    brew install python3
    ```
   
2. Clone this repository:
    ```sh
    git clone https://github.com/anthonyfer0220/folder-syncer.git
    ```

## Usage

1. Navigate to the project directory:
    ```sh
    cd folder-syncer/folder_syncer
    ```
   
2. Run the script:
    ```sh
    python3 main.py "/path/to/source" "/path/to/destination"
    ```

3. Optional: A skip flag can be used to ignore specific files and/or folders in the synchronization process
    ```sh
    -s or --skip
    ```

### Example

To synchronize `source_folder` with `destination_folder`, run:

```sh
python3 main.py "~/source_folder" "~/destination_folder"
```

or

```sh
python3 main.py "/Users/your_username/source_folder" "/Users/your_username/destination_folder"
```

To skip `test_file.py` and `test_folder`:

```sh
python3 main.py "~/source_folder" "~/destination_folder" -s test_file.py test_folder
```

or

```sh
python3 main.py "~/source_folder" "~/destination_folder" --skip test_file.py test_folder
```

### Notes

- Ensure both source and destination paths are accessible and writable.
- Synchronization logs are automatically stored in the `folder_syncer/logs/` directory, which is created if it does not already exist.
- Suggestion: Consider creating shell functions for frequently synchronized folders:

```sh
sync_folder_1() {
    cd "$HOME/Developer/folder-syncer/folder_syncer" || return
    python3 main.py "~/source_folder" "~/destination_folder" -s test_file.py test_folder
}
```

## Contributing

Contributions are welcome. Feel free to open a pull request or submit issues.

## License

[MIT License](LICENSE) © Anthony Fernandez