import os
from pathlib import Path

def organize_files(directory):
   
    file_extensions = set()
    
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extensions.add(filename.split('.')[-1].lower())

    for extension in file_extensions:
        extension_dir = os.path.join(directory, extension)
        os.makedirs(extension_dir, exist_ok=True)

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            source_path = os.path.join(directory, filename)
            destination_path = os.path.join(directory, filename.split('.')[-1].lower(), filename)
            os.rename(source_path, destination_path)
            print(f"Moved {filename} to {filename.split('.')[-1].lower()} directory")
directory_to_organize = "c:\Users\HP\Downloads"

if os.path.exists(directory_to_organize):
    organize_files(directory_to_organize)
    print("Organizing complete.")
else:
    print("Directory does not exist.")