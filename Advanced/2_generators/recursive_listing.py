from os import listdir
from os.path import isfile, join, exists, isdir


# print(listdir(r"C:\kdata\myPYTHON\MyLearnings\Python_Scripts\tkinter"))
# print("".join("apple"))  # normal join under string
# print(join(r"C:\kdata\myPYTHON\MyLearnings\Python_Scripts\tkinter", "entry.py"))


def get_files(path):
    for file in listdir(path):
        full_path = join(path, file)
        if isfile(full_path):
            if exists(full_path):
                yield full_path


def get_directories(path):
    for directory in listdir(path):
        full_path = join(path, directory)
        if isdir(full_path):
            if exists(full_path):
                yield full_path


# def get_files_recursively(directory):
#     for file in get_files(directory):
#         yield file
#     for subdirectory in get_directories(directory):
#         for file in get_files_recursively(subdirectory):
#             yield file

# simplified version of above function


def get_files_recursively(directory):
    yield from get_files(directory)
    for subdirectory in get_directories(directory):
        yield from get_files_recursively(subdirectory)


files = get_files_recursively(r"C:\kdata\myPYTHON\MyLearnings\Python_Scripts\tkinter")

for file in files:
    print(file)
