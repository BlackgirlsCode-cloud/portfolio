"""
auto_folder_cleaner.py
Deletes temporary or duplicate files from a folder based on file extension or name patterns.

Author: [Your Name]
"""

import os

def clean_folder(folder_path: str, extensions_to_delete=None):
    """
    Deletes files with specified extensions from a folder.
    Example: clean_folder('downloads', ['.tmp', '.bak'])
    """
    if extensions_to_delete is None:
        extensions_to_delete = ['.tmp', '.bak']

    try:
        removed_files = 0
        for file in os.listdir(folder_path):
            if any(file.endswith(ext) for ext in extensions_to_delete):
                os.remove(os.path.join(folder_path, file))
                removed_files += 1
        print(f"✅ Deleted {removed_files} files from '{folder_path}'")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    clean_folder("downloads", ['.tmp', '.bak'])
