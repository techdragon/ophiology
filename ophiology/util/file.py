import os
import fnmatch
import re
import tempfile

def find_absolute_filenames(directory, pattern):
    '''This function recursively finds all files in a
     given directory tree that match a given pattern'''
    # TODO: do something with the dirs variable to clean this up better
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def find_relative_filenames(directory, pattern):
    '''This function recursively finds all files in a
     given directory tree that match a given pattern'''
    # TODO: do something with the dirs variable to clean this up better
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.relpath(
                    os.path.join(root, basename), directory)
                yield filename

# def find_files(directory, pattern):
#     '''This function recursively finds all files in a
#      given directory tree that match a given pattern'''
#     for root, dirs, files in os.walk(directory):
#         for basename in files:
#             if fnmatch.fnmatch(basename, pattern):
#                 filename = os.path.join(root, basename)
#                 # filename = os.path.relpath(
#                 #     os.path.join(root, basename), directory)
#                 yield filename
