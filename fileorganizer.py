#Import os Module
from fileinput import filename
import os
#Import shutil Module
import shutil
#Import Datetime Module
from datetime import datetime
#File Category list
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', ".ico "],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.odt', '.ods', '.odp', '.rtf', '.csv', ".doc", ".md", "xls", ".ppt", "pptx", ".xlsx"],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv',  '.wmv', '.webm', '.mpeg', '.mpg', '.3gp', '.ogg'],
    'Archives': ['.zip', '.rar', '.tar.gz', '.7z', '.gz', '.bz2', '.xz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.cs', '.php', '.rb', '.go', '.ts', '.tsx', '.jsx', '.json', '.xml', '.yml', '.yaml', '.sh', '.bat', '.ps1', '.xml'],
    'Executables': ['.exe', '.msi', '.apk', '.bat', '.sh', '.bin', '.app', '.deb', '.rpm'],
}
#Function to scan folder and folder path
def scan_folder(folder_path):
    #Check if the folder path exists
    all_items = os.listdir(folder_path)
    files = []
    for item in all_items:
        full_path = os.path.join(folder_path, item)
        is_file = os.path.isfile(full_path)
        is_hidden = item.startswith('.')
        if is_file and not is_hidden:
            files.append(full_path)
    return files

#Function to organize files by file names
def organize_files(folder_path):
    files = scan_folder(folder_path)
    for file_path in files:
        _, extension = os.path.splitext(file_path)
        extension = extension.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"   
#Function to move files to new folder
def move_file(filename, source_folder, category, dry_run=False):
    source_path = os.path.join(source_folder, filename)
    dest_folder = os.path.join(source_folder, category)
    dest_path   = os.path.join(dest_folder, filename)

    # Handle filename conflicts — don't overwrite existing files
    if os.path.exists(dest_path):
        name, ext   = os.path.splitext(filename)
        timestamp   = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename    = f"{name}_{timestamp}{ext}"
        dest_path   = os.path.join(dest_folder, filename)
    if dry_run:
        return(f" [DRY RUN] Would move: {source_path} -> {dest_path}")
    try:
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(source_path, dest_path)
        return(f" Moved: {source_path} -> {dest_path}")
    except Exception as e:
        return(f" Error moving {source_path} to {dest_path}: {e}")