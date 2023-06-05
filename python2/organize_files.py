import os
import shutil

def create_directory_if_not_exists(directory_path):
    """Create the directory if it does not exist."""
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    except Exception as e:
        print(f"Failed to create directory {directory_path}. Error: {e}")

def move_file_to_directory(file, directory_path):
    """Move the file to the target directory."""
    try:
        shutil.move(file, directory_path)
    except Exception as e:
        print(f"Failed to move file {file} to {directory_path}. Error: {e}")

def organize_files_by_extension(source_directory):
    """Organize the files in the directory by their extension."""
    if os.path.exists(source_directory):
        for file_name in os.listdir(source_directory):
            # Ignore directories, only process files
            if os.path.isfile(os.path.join(source_directory, file_name)):
                # Get file extension
                file_extension = os.path.splitext(file_name)[1].lower()
                if file_extension:
                    # Create a directory path
                    directory_path = os.path.join(source_directory, file_extension)
                    
                    # Create the directory
                    create_directory_if_not_exists(directory_path)
                    
                    # Move the file
                    move_file_to_directory(os.path.join(source_directory, file_name), directory_path)
    else:
        print(f"Source directory {source_directory} does not exist")

if __name__ == "__main__":
    source_directory = "<diretorio_aqui>"
    organize_files_by_extension(source_directory)
