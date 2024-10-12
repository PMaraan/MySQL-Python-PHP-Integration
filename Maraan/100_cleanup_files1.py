import os

# List of files to be removed
files_to_remove = [
    '04_output.xml',  # Change these paths to your file paths
    'output.csv'
    ]

for file_to_remove in files_to_remove:
    try:
        # Check if the file exists
        if os.path.isfile(file_to_remove):
            os.remove(file_to_remove)
            print(f"{file_to_remove} has been removed successfully.")
        else:
            print(f"The file {file_to_remove} does not exist.")
    except Exception as e:
        print(f"An error occurred while trying to remove {file_to_remove}: {e}")