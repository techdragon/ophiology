
import json
from pprint import pprint
from pprint import pformat
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import os
import fnmatch

import envoy
import click

from ophiology.util.file import find_relative_filenames
from ophiology.util.log import LOGGING
from ophiology.util.misc import message_level_from_code

# def find_files(directory, pattern):
#     for root, dirs, files in os.walk(directory):
#         for basename in files:
#             if fnmatch.fnmatch(basename, pattern):
#                 # filename = os.path.join(root, basename)
#                 filename = os.path.relpath(os.path.join(root, basename), directory)
#                 yield filename

def prospector_cmd(path):
    """..."""
    LOGGING.debug('Called with path: {}', path)
    LOGGING.debug('Current working directory: {}', os.getcwd())
    return 'prospector -o json .'

def run_prospector(path):
    return envoy.run(prospector_cmd(path))

def prospector_output(path):
    return run_prospector(path).std_out


class FailingFile(object):
    """docstring for FailingFile"""
    def __init__(self, filename, messages, arg):
        super(FailingFile, self).__init__()
        self.arg = arg
        self.filename = filename
        self.messages = messages
    filename = ''
    messages = {}


def execute():
    files = []

    for filename in find_relative_filenames(os.getcwd(), '*.py'):
        # LOGGING.debug('Found Python source: {}', filename)
        files.append(filename)

    prospector_result = prospector_output(os.getcwd())

    # LOGGING.debug('Prospector JSON Result:\n{}', prospector_result)

    LINTER_RESULTS = json.loads(prospector_result)
    # pprint(LINTER_RESULTS)

    LINTER_MESSAGE_SOURCES = set()
    LINTER_MESSAGES = {}
    FILE_MESSAGES = {}

    for index, i in enumerate(LINTER_RESULTS['messages']):
        # LOGGING.debug("ITEM #{} : {}", str(index), i)
        try:
            LINTER_MESSAGES[i['source']].append(i)
        except KeyError:
            LINTER_MESSAGES[i['source']] = []
            LINTER_MESSAGES[i['source']].append(i)

    for index, i in enumerate(LINTER_RESULTS['messages']):
        # LOGGING.debug("ITEM #{} : {}", str(index), i)
        # click.echo("ITEM #%s : %s" % (str(index), i))
        try:
            FILE_MESSAGES[i['location']['path']].append(i)
        except KeyError:
            FILE_MESSAGES[i['location']['path']] = []
            FILE_MESSAGES[i['location']['path']].append(i)

    for key, value in LINTER_MESSAGES.iteritems():
        LINTER_MESSAGE_SOURCES.add(key)

    # click.echo(pformat(FILE_MESSAGES))


    CHECKSTYLE = ET.Element('checkstyle', {'version':'5.0',})

    for _file in files:
        FILE = ET.SubElement(CHECKSTYLE, 'file', {'name': str(_file)})
        messages = FILE_MESSAGES.get(str(_file))
        if messages:
            for message in messages:
                ERROR = ET.SubElement(FILE, 'error', {
                    'line': str(message['location']['line']),
                    'column': str(message['location']['character']),
<<<<<<< HEAD
                    'message': message['code'],

                    'severity': message_level_from_code(message['code']),
                    'source': (str(message['location']['module']) + '::' +
                               str(message['location']['function']))
                })
                ERROR.text(message['message'])
=======
                    'message': message['message'],
                    'severity':'',
                    'source': (str(message['location']['module']) + '::' +
                               str(message['location']['function']))
                })
>>>>>>> 5b0be70f9ce3d2cdb1fee44c518f1372f39a3084
        # click.echo(pformat(messages))

    OUTPUT = ET.tostring(CHECKSTYLE)

    # pprint(OUTPUT)
    # pprint(LINTER_MESSAGE_SOURCES)
    xml = parseString(OUTPUT)
    pretty_xml_as_string = xml.toprettyxml()
    # LOGGING.debug(pretty_xml_as_string)
    click.echo(pretty_xml_as_string)
    output_file = open('checkstyle.xml', 'w')
    output_file.write(pretty_xml_as_string)
    output_file.close()
    # click.echo_via_pager(prospector_result)
    # click.echo_via_pager(pretty_xml_as_string)



# pprint(LINTER_MESSAGES)

# <checkstyle version="5.0">
#     <file name="C:\Workspace\default_ant\src\org\sprunck\bee\Bee.java">
#     </file>
#     <file name="C:\Workspace\default_ant\src\org\sprunck\bee\package-info.java">
#     </file>
#     <file name="C:\Workspace\default_ant\src\org\sprunck\foo\Foo.java">
#         <error line="10" message="Line has trailing spaces." severity="error" source="com.puppycrawl.tools.checkstyle.checks.regexp.RegexpSinglelineCheck"></error>
#         <error line="20" message="Line has trailing spaces." severity="error" source="com.puppycrawl.tools.checkstyle.checks.regexp.RegexpSinglelineCheck"></error>
#         <error column="26" line="30" message="'Went' entspricht nicht dem Muster '^[a-z][a-zA-Z0-9]*$'." severity="error" source="com.puppycrawl.tools.checkstyle.checks.naming.MethodNameCheck"></error>
#     </file>
#     <file name="C:\Workspace\default_ant\src\org\sprunck\foo\package-info.java">
#     </file>
#     <file name="C:\Workspace\default_ant\src\org\sprunck\tests\BeeTest.java">
#     </file>
#     <file name="C:\Workspace\default_ant\src\org\sprunck\tests\FooTest.java">
#     </file>
#     <file name="C:\Workspace\default_ant\src\org\sprunck\tests\package-info.java">
#     </file>
# </checkstyle>
