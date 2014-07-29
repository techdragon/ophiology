import json
from pprint import pprint
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os, fnmatch

import envoy


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                # filename = os.path.join(root, basename)
                filename = os.path.relpath(os.path.join(root, basename), directory)
                yield filename

files = []

for filename in find_files(os.getcwd(), '*.py'):
    print 'Found Python source:', filename
    files.append(filename)

with open('input.json') as json_data:
    LINTER_RESULTS = json.load(json_data)
    json_data.close()
    # pprint(LINTER_RESULTS)

LINTER_MESSAGE_SOURCES = set()
LINTER_MESSAGES = {}

for index, i in enumerate(LINTER_RESULTS['messages']):
    # print "ITEM #%s " % str(index), i
    try:
        LINTER_MESSAGES[i['source']].append(i)
    except KeyError:
        LINTER_MESSAGES[i['source']] = []
        LINTER_MESSAGES[i['source']].append(i)

for key, value in LINTER_MESSAGES.iteritems():
    LINTER_MESSAGE_SOURCES.add(key)


CHECKSTYLE = ET.Element('checkstyle', {'version':'5.0',})

for filename in files:
    FILE = ET.SubElement(CHECKSTYLE, 'file', {'name': str(filename)})

OUTPUT = ET.tostring(CHECKSTYLE)

# pprint(OUTPUT)
# pprint(LINTER_MESSAGE_SOURCES)
xml = xml.dom.minidom.parseString(OUTPUT)
pretty_xml_as_string = xml.toprettyxml()

print pretty_xml_as_string



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
