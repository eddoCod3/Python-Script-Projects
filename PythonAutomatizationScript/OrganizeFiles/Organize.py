import os
import shutil
import sys


# Set the directory to search for files
directory = '/directory of your files'

# Set the destination directory to move the files to
destination_directory = '/directory of  output'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1]

    # Check if the file has one of the specified extensions
    if file_extension.lower() in [ ".png", ".jpg",  ".mp4",  ".pdf ",  ".mp3", ".jpeg",".rar" ,".zip",".ppt" , ".wav" , ".ogg" ,".psd",".psd" ,".epub" ,".pptx" , ".gif"]:
        # If the file has one of the specified extensions, move it to the destination directory
        source_file_path = os.path.join(directory, filename)
        destination_folder_path = os.path.join(destination_directory, file_extension[1:].lower())
        destination_file_path = os.path.join(destination_folder_path, filename)
        if not os.path.exists(destination_folder_path):
            os.makedirs(destination_folder_path)
        shutil.move(source_file_path, destination_file_path)

print("Files Organized :D")