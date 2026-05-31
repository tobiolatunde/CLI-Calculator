#Import os Module
from fileinput import filename
from importlib.resources import files
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
    #Function to log file movements
def log_move(log_path, message):
    timestamp = datetime.now().isoformat()
    entry = f"{timestamp} - {message}"
    with open(log_path, 'a') as f:
        f.write(entry)
        #Function to print preview of file movements
def preview_preview(files):
    print ()
    print("Preview of file movements:")
    print(f"{'Source':<40} {'Destination':<40} {'Status'}")
    for filename in files:
        category = organize_files(filename)
        message = move_file(filename, os.path.dirname(filename), category, dry_run=True)
        print(message)
        #Function To Print Summary of file movements
def print_summary(moved, skipped, errors):
    total = moved + skipped + errors
    print("\nSummary of file movements:")
    summary = {}
    for filename in files:
        category = organize_files(filename)
        summary[category] = summary.get(category, 0) + 1
    for category, count in summary.items():
        print(f"{category}: {count} files")
        #Function to organize files in folder
def run_organizer(folder_path, dry_run=False):
    log_path = os.path.join(folder_path, "file_organizer.txt")
    files = scan_folder(folder_path)
    moved, skipped, errors = 0, 0, 0
    for filename in files:
        category = organize_files(filename)
        message = move_file(filename, folder_path, category, dry_run=dry_run)
        log_move(log_path, message)
        if "Moved:" in message:
            moved += 1
        elif "Would move:" in message:
            skipped += 1
        else:
            errors += 1
    print_summary(moved, skipped, errors)
    #Function to get folder path from user input
def get_folder_path():
    while True:
        raw = input("Enter the folder path to organize (or 'exit' to quit): ").strip()
        if os.path.isdir(raw):
            return raw
        print(f"\nInvalid folder path: {raw}")
        print("Please enter a valid folder path or type 'exit' to quit.")
        #Function to get mode (dry run or actual) from user input
def get_mode():
    while True:
        mode = input("Choose mode: [1] Dry Run (preview only) or [2] Actual Move: ").strip()
        if mode == '1':
            return True
        elif mode == '2':
            return False
        print("\nInvalid choice. Please enter '1' for Dry Run or '2' for Actual Move.")
        #Main function to run the file organizer
def main():
    print()
    print("  ╔══════════════════════════════════════╗")
    print("  ║         CLI FILE ORGANISER           ║")
    print("  ║         Phase 1 — Python             ║")
    print("  ╚══════════════════════════════════════╝")
    print()
    print("  This program sorts files in a folder into")
    print("  subfolders by type (Images, Videos, Documents...)")

    folder_path = get_folder_path()
    dry_run = get_mode()
    run_organizer(folder_path, dry_run=dry_run)
    print()
    again = input("Do you want to organize another folder? (y/n): ").strip().lower()
    if again == 'y':
        print()
        print("File Sorted!")
        print()
    #Entry point
if __name__ == "__main__":
    main()