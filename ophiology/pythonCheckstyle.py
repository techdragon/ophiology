import os, fnmatch

import envoy

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                # filename = os.path.join(root, basename)
                filename = os.path.relpath(os.path.join(root, basename), directory)
                yield filename


for filename in find_files(os.getcwd(), '*.py'):
    print 'Found Python source:', filename
    command = 'python -m mccabe %s' % filename
    cmd = envoy.run(command)
    print cmd.std_out
