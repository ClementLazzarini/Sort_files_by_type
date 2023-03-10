import pathlib
import shutil


def sort_files_by_type(work_dir):
    """Sort files in a directory into subdirectories by type

    Args:
        work_dir (pathlib.Path): Path to directory to sort
    """
    # Define file types and corresponding directories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Musiques": [".mp3", ".wav", ".flac", ".m4a"],
        "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Autres": []
    }

    # Create directories for each file type
    for dir_name in file_types.keys():
        dir_path = work_dir / dir_name
        dir_path.mkdir(exist_ok=True)

    # Move files to corresponding directories based on file type
    for file in work_dir.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            moved = False

            # Move file to corresponding directory
            for dir_name, extensions in file_types.items():
                if ext in extensions:
                    dir_path = work_dir / dir_name
                    shutil.move(str(file), str(dir_path / file.name))
                    moved = True
                    break

            # If file type not found, move to "Autres" directory
            if not moved:
                autres_path = work_dir / "Autres"
                shutil.move(str(file), str(autres_path / file.name))


if __name__ == "__main__":
    work_dir = pathlib.Path(input("Insert the path to the folder: "))
    sort_files_by_type(work_dir)
