from pathlib import Path
import shutil

def ask_bool(prompt: str) -> bool:
    return input(f'{prompt} (y/n):').strip().lower() == 'y'

def unique_destination_path(dest: Path) -> Path:
    if dest.exists():
        return dest
    stem = dest.stem #the stem is the file name without the extension
    suffix = dest.suffix #the suffix is the file extension
    parent = dest.parent #the parent is the directory that the file exists in
    counter = 1
    while True:
        candidate = parent / f'{stem}{counter}{suffix}'
        if not candidate.exists():
            return candidate
        counter += 1
def is_already_in_target(file_path: Path, root: Path,target_folder:str) -> bool:
    try:
        rel = file_path.relative_to(root)
    except Exception:
        return False
    parts = [p.lower() for p in rel.parts]
    return len(parts) >= 2 and parts[0] == target_folder.lower()

def enumerate_files(root: Path, recursive: bool):
    if recursive:
        yield from (p for p in root.rglob("*") if p.is_file()) #.rglob searches for files recursively
    else:
        yield from (p for p in root.iterdir() if p.is_file()) #.iterdir searches for files directly in the directory

def organize_by_extension(root: Path, recursive: bool):
    moved = 0
    skipped = 0
    errors = 0

    for f in enumerate_files(root, recursive):
        ext = f.suffix.lower().lstrip('.') or 'other'
        target_dir = root / ext
        if is_already_in_target(f, root, ext):
            skipped += 1
            continue

        target_dir.mkdir(parents=True, exist_ok=True) #dir.mkdir creates a directory
        dest = unique_destination_path(target_dir / f.name)
        try:
            shutil.move(str(f), str(dest))
            moved += 1
            print(f'Moved {f} -> {dest}')
        except Exception as e:
            errors += 1
            print(f'Error moving {f}: {e}')

    print('\nSummary:')
    print(f'- Moved: {moved}')
    print(f'- Skipped: {skipped}')
    print(f'- Errors: {errors}')

def main():
    print('Welcome to the file organizer Application')
    path_str = input('Enter the path to the folder you want to organize: ').strip().strip('"')
    root = Path(path_str)

    if not root.exists() or not root.is_dir():#exists checks if the path exists and is a directory
        print(f'Error: {root} is not a valid directory')
        return

    recursive = ask_bool('Include subfolder?')
    if not ask_bool('Continue?'):
        print('Cancelled')
        return

    organize_by_extension(root, recursive)

if __name__ == '__main__':
    main()







