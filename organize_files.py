import os
import shutil

def organize_files(directory):
    # Dictionary to map file extensions to folder names
    file_types = {
        "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff"],
        "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
        "Documents": [".pdf", ".docx", ".doc", ".ppt", ".xls", ".xlsx", ".txt"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Others": []
    }

    # Ensure the provided directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    # Create folders for each file type
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their corresponding folders
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        _, ext = os.path.splitext(file)
        ext = ext.lower()
        
        # Find the appropriate folder
        folder_moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(directory, folder))
                folder_moved = True
                break

        # Move to "Others" if the file type is not categorized
        if not folder_moved:
            shutil.move(file_path, os.path.join(directory, "Others"))

    print(f"Files in {directory} have been organized!")

# Specify the directory you want to organize
if __name__ == "__main__":
    path = input("Enter the path to the folder you want to organize: ").strip()
    organize_files(path)
