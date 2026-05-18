#Import os Module
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