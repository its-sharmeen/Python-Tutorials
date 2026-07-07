
#  WAP to print contents of directory using OS module.Search online for function which does that

import os

# Define the target directory path (use '.' for the current working directory)
directory_path = '.'

try:
    # Retrieve all files and folders in the specified directory
    directory_contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in directory_contents:
        print(item)
        
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to access '{directory_path}'.")
