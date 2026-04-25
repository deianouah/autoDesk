import os
import shutil

# 1. Define the source directory (Downloads folder)
# Using 'r' before the string to handle backslashes in Windows
downloads_path = r"C:\Users\user\Downloads"

# 2. Map folders to their respective file extensions
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Zipped": [".zip", ".rar", ".7z"]
}

# 3. Create target folders if they do not exist
for folder in folders.keys():
    folder_path = os.path.join(downloads_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 4. Iterate through every file in the Downloads folder
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    
    # Check if the path is a file (ignore directories)
    if os.path.isfile(file_path):
        # Get the file extension and convert to lowercase
        extension = os.path.splitext(filename)[1].lower()
        
        # 5. Find the matching folder for the extension
        for folder, extensions in folders.items():
            if extension in extensions:
                # Define the destination path
                destination = os.path.join(downloads_path, folder, filename)
                
                # Move the file
                shutil.move(file_path, destination)
                print(f"Success: Moved {filename} to {folder}")