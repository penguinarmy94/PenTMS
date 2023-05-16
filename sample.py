import os
from typing import Tuple, List

tuple_of_extensions = (".html", ".cpp", ".xml", ",doc", "txt", "py")

def find_files_with_extension(directory: str, depth: int = 0, extension: str = tuple_of_extensions) -> Tuple[str]:
    """
        Recursively find files with a specific extension
        
        Args:
            directory (str): the directory to traverse
            depth (int, optional): the level of subdirectories to traverse. Default is to not traverse subdirectories '0'
            extension (str, optional): the extension to look for. Default is '.txt'.
        
        Return:
            Tuple[str]: the list of full paths to files within the directory that match the extension rule
    """
    
    files: List[str] = []
    
    for file_object in os.scandir(directory):
        if file_object.is_file() and file_object.name.endswith(extension):
            files.append(file_object.path)
        elif file_object.is_dir() and depth > -1:
            files.extend(find_files_with_extension(directory=file_object.path, depth=depth-1, extension=extension))
        else:
            continue
    
    return tuple(files)


if __name__ == "__main__":
    directory: str =  r"C:\Users\marti\PythonProjects"
    files: Tuple[str] = find_files_with_extension(directory=directory, depth=3, extension=(".txt", ".html", ".cpp"))
     
    print(files)
 

