# from __future__ import print_functionx`
import os
import re

from tempfile import NamedTemporaryFile

import envoy

from ophiology.util.file import find_absolute_filenames
from ophiology.util.log import LOGGING


EXCLUDES = (
    re.compile(r'''/migrations/[0-9]{4,}'''),
    re.compile(r'''/migrations/__init__\.py'''),
    # re.compile(r'''tests\.py'''),
    re.compile(r''' (?:^|[b_.-])[Tt]est'''),
)

def excluded(filename):
    '''Test filenames against the exclusion parameters'''
    for exclude_regex in EXCLUDES:
        if exclude_regex.search(filename):
            return True
    return False


# IGNORE_DIRS = ['--ignore-dir=%s' % _dir
#                for _dir in set([os.path.dirname(_file)
#                                 for _file in find_files(os.getcwd(), '*.py')
#                                 if EXCLUDE.search(_file)])]


def execute():
    """Run the clonedigger application"""
    files = []
    # IGNORE_DIRS = set()

    tempfile = NamedTemporaryFile()
    LOGGING.debug(tempfile)
    LOGGING.debug(tempfile.name)
    LOGGING.info('Python source code files to be checked for duplicate code' +
        ' are stored in tempfile {}', tempfile.name)

    files = [_file for _file in find_absolute_filenames(os.getcwd(), '*.py')
         if not excluded(_file)]

    for _file in files:
        print _file
        tempfile.write("%s\n" % _file)


    command = ' '.join([
        'clonedigger',
        '--cpd-output',
        '--file-list=%s' % tempfile.name
    ])

    print command

    process = envoy.run(command)
    print process.std_out
