"""
auto_folder_cleaner.py
Deletes temporary or duplicate files from a folder based on file extensions.

Author: Gracie
"""

from pathlib import Path
from typing import List, Optional
import argparse

def clean_folder(folder_path: str, extensions_to_delete: Optional[List[str]] = None) -> None:
    """
    Deletes files with specified extensions from a folder.

    Args:
        folder_path (str): Path to the folder to clean.
        extensions_to_delete (List[str], optional): List of file extensions to delete. Defaults to ['.tmp', '.bak'].
    """
    if extensions_to_delete is None:
        extensions_to_delete = ['.tmp', '.bak']

    folder = Path(folder_path)
    removed_files = 0

    try:
        for file_path in folder.iterdir():
            if file_path.is_file() and file_path.suffix in extensions_to_delete:
                file_path.unlink()
                removed_files += 1
        print(f"✅ Deleted {removed_files} files from '{folder_path}'")
    except Exception as e:
        print(f"❌ Error cleaning folder '{folder_path}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clean folder by deleting files with specific extensions.')
    parser.add_argument('folder', help='Path to the folder to clean')
    parser.add_argument('-e', '--extensions', nargs='+', default=['.tmp', '.bak'], help='File extensions to delete (e.g., .tmp .bak)')
    args = parser.parse_args()

    clean_folder(args.folder, args.extensions)
