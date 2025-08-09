from pathlib import Path

def ask_bool(prompt: str) -> bool:
    return input(f'{prompt}(y/n):').strip().lower() == 'y'
def delete_empty_directories(root: Path, recursive: bool):
    deleted_directories = 0
    failed_directories = 0
    if not recursive:
        try:
            for z in root.iterdir():#iterdir searches for files directly in the root
                if z.is_dir():#.is_dir checks if the directory is a directory
                    if len(list(z.iterdir())) == 0: #checks if the directory is empty
                        deleted_directories += 1
                        print(f'Deleting empty directory: {z}')
                        z.rmdir() #.rmdir() deletes files
                        print(f'Deleted {deleted_directories} empty directories')
        except Exception as e:
            print(e)
            failed_directories += 1
            print(f'Failed to delete {failed_directories} directories')

    else:
        try:
            for f in root.rglob('*'): #rglob searches for files recursively
                if f.is_dir(): #is_dir checks if the directory is a directory

                    if len(list(f.iterdir())) == 0: #Converts into a list and checks if the directory is empty
                        deleted_directories += 1
                        print(f'Deleting empty file: {f}')
                        f.rmdir() #.rmdir() deletes directory
                        print(f'Deleted {deleted_directories} empty directories')
        except Exception as e:
            print(e)
            failed_directories = 0
            failed_directories += 1
            print(f'Failed to delete {failed_directories} directories')

def main(): #main should never have any arguments or parameters
    print('Welcome to the directory deletion program')
    root = Path(input('Enter the root of the directory that you want to delete:'))
    if not root.exists():
        print(f'Error: {root} does not exist')
        return
    if not root.is_dir():
        print(f'Error: {root} is not a directory')
    print(f'Directory: ', root.resolve(), 'found')
    recursive = ask_bool('Do you want to delete subdirectories?')
    delete_empty_directories(root, recursive)

if __name__ == '__main__':
    main()


