"""Django utilities."""
import inspect
import os
import sys
from tempfile import NamedTemporaryFile

def django_apps(django_settings_file):
    try:
        import imp
        code = imp.load_source('django.settings', django_settings_file)
        # or name, obj in inspect.getmembers(code)
        print dir(code)
    except ImportError as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        # TODO: Fix this so its safer.
        # http://stackoverflow.com/questions/1278705/python-when-i-catch-an-exception-how-do-i-get-the-type-file-and-line-number#comment1121378_1278740
        # print dir(code)

        pre_error_slice_file = NamedTemporaryFile()

        with open(django_settings_file) as _file1:
            pre_error_slice = [next(_file1) for x in xrange(exc_tb.tb_lineno)]
        pre_error_slice_file.write(str(pre_error_slice))

        try:
            import imp
            code = imp.load_source('django.settings', pre_error_slice_file.name)
            # or name, obj in inspect.getmembers(code)
            print dir(code)
            print inspect.getsourcelines(code)
        except ImportError:
            print "Unable to load a working fragement of the specified file"



