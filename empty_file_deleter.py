from pathlib import Path
import os

def ask_bool(prompt: str) -> bool:
    return input(f'{prompt}(y/n):').strip().lower() == 'y'

def delete_empty_files(root: Path, recursive: bool):
    if not recursive:
        try:
            for z in root.iterdir():#iterdir searches for files directly in the root
                if z.is_file():#is_file checks if the file is a file
                    if z.stat().st_size == 0:#.stat().st_size returns the size of the file in bytes
                        print(f'Deleting empty file: {z}')
                        z.unlink() #.unlink deletes files
                        deleted_files = 0
                        deleted_files += 1
                        print(f'Deleted {deleted_files} empty files')
        except Exception as e:
            print(e)
            failed_files = 0
            failed_files += 1
            print(f'Failed to delete {failed_files} files')

    else:
        try:
            for f in root.rglob('*'): #rglob searches for files recursively
                if f.is_file(): #is_file checks if the file is a file
                    if f.stat().st_size == 0: #.stat().st_size returns the size of the file in bytes
                        print(f'Deleting empty file: {f}')
                        f.unlink() #.unlink deletes files
                        deleted_files = 0
                        deleted_files += 1
                        print(f'Deleted {deleted_files} empty files')
        except Exception as e:
            print(e)
            failed_files = 0
            failed_files += 1
            print(f'Failed to delete {failed_files} files')
def main():
    print('This program will delete empty files in a directory')
    root = Path(input('Enter the root directory you want to clean: '))
    if not root.exists(): #makes sure the path exists
        print(f'Error: {root} does not exist')
        return
    if not root.is_dir(): #makes sure the path is a directory
        print(f'Error: {root} is not a directory')
    print(f'Directory: {root.resolve} found')
    recursive = ask_bool('Include subfolders?')
    confirm = ask_bool('Continue?')
    if not confirm:
        print('Cancelled')
        return
    delete_empty_files(root, recursive)


if __name__ == '__main__':
    main()


