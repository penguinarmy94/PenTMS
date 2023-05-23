import unittest
import os
import pathlib
import sys
import random
from typing import Tuple, List

# This is to be able to import from parent package
sys.path.append(os.path.abspath(".."))
from PenTMS import sample

FILE_EXTENSIONS = (".txt", ".py", ".cpp", ".pdf", ".rd", ".bat", ".yml", ".xml", ".lppr", ".ov", ".cs", ".h")
NAME_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MODULE_DIR_FOR_UNITTEST = os.path.abspath(".")

def create_random_filename(character_count: int = 5):
    filename: str = ""

    for _ in range(character_count):
        char_index: int = random.randint(0,len(NAME_CHARS)-1)
        filename += NAME_CHARS[char_index]
    
    return filename

def create_random_folder_structure(base_dir: str, dir_name: str, subdir_depth: int = 5, max_files_per_subdir: int = 10, override: bool = False):
    base_path: pathlib.Path = pathlib.Path(base_dir)
    base_path = base_path / dir_name
    files_created: List[str] = []

    if base_path.exists() and override == False:
        return []
    if base_path.is_dir():
        delete_path_recursive(file_path=str(base_path))
    
    os.makedirs(base_path)
    number_of_files: int = random.randint(1,max_files_per_subdir)
    number_of_subdirs: int = random.randint(0,max_files_per_subdir-number_of_files)

    for _ in range(number_of_files):
        extension_index: int = random.randint(0,len(FILE_EXTENSIONS)-1)
        extension: str = FILE_EXTENSIONS[extension_index]
        name: str = create_random_filename(character_count=random.randint(3,20)) + extension
        file_path: pathlib.Path = base_path / name

        with open(file_path, "w") as writer:
            writer.write("...")
        
        files_created.append(str(file_path))
    
    if subdir_depth <= 0:
        return files_created
    
    for _ in range(number_of_subdirs):
        name: str = create_random_filename(character_count=random.randint(3,20))
        create_random_folder_structure(
            base_dir=str(base_path), 
            dir_name=name, 
            subdir_depth=subdir_depth-1, 
            max_files_per_subdir=max_files_per_subdir
        )
    
    return files_created

def delete_path_recursive(file_path: str):
    if not os.path.isdir(file_path) and os.path.exists(file_path):
        os.unlink(file_path)
    elif not os.path.exists(file_path):
        raise FileNotFoundError(f"The path '{file_path}' does not exist")
    else:
        for subfile_path in os.scandir(file_path):
            delete_path_recursive(file_path=subfile_path)
        
        os.rmdir(file_path)

class TestExtensions(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__subdir_depth: int = 5
        self.__max_files_per_subdir: int = 10
        self.__extensions: Tuple[str] = (".html", ".txt", ".py")

        self.__files_created: List[str] = create_random_folder_structure(
            base_dir=MODULE_DIR_FOR_UNITTEST, 
            dir_name="TestDir", 
            subdir_depth=self.__subdir_depth, 
            max_files_per_subdir=self.__max_files_per_subdir, 
            override=True
        )
    
    @classmethod
    def tearDownClass(cls):
        delete_path_recursive(file_path=os.path.join(MODULE_DIR_FOR_UNITTEST, "TestDir"))

    def test_extensions_match(self):
        sample_dir: str = os.path.join(MODULE_DIR_FOR_UNITTEST, "TestDir")
        sample_depth: int = -1
        files: Tuple[str] = sample.find_files_with_extension(directory=sample_dir, depth=sample_depth, extensions=self.__extensions)

        for file in files:
            file_path: pathlib.Path = pathlib.Path(file)
            self.assertIn(file_path.suffix, self.__extensions)

    def test_filelist_size(self):
        sample_dir: str = os.path.join(MODULE_DIR_FOR_UNITTEST, "TestDir")
        sample_depth: int = -1
        files: Tuple[str] = sample.find_files_with_extension(directory=sample_dir, depth=sample_depth, extensions=self.__extensions)

        self.assertLessEqual(len(files), len(self.__files_created))

if __name__ == "__main__":
    unittest.main()

