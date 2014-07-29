import json
from pprint import pprint
import xml.etree.ElementTree as ET
import xml.dom.minidom

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


TESTSUITES = ET.Element('testsuites', {
    'name':'prospector',
    'tests':str(LINTER_RESULTS['summary']['message_count']),
    'time':str(LINTER_RESULTS['summary']['time_taken'])})

for i in xrange(len(LINTER_MESSAGE_SOURCES)):
    linter_type = LINTER_MESSAGE_SOURCES.pop()
    TESTSUITE = ET.SubElement(
        TESTSUITES, 'testsuite', {
            'name': linter_type,
            'tests':str(len(LINTER_MESSAGES[str(linter_type)]))})
    for index, j in enumerate(LINTER_MESSAGES[linter_type])
        TESTCASE = ET.SubElement(
            TESTSUITE, 'testcase', {'classname':'foo', 'name':})

        # TESTCASE = ET.SubElement(
        #     TESTSUITE, 'testcase', {'classname':'foo', 'name':'ASuccessfulTest'})
# PROPERTIES = ET.SubElement(TESTSUITE, 'properties')
OUTPUT = ET.tostring(TESTSUITES)

# pprint(OUTPUT)
# pprint(LINTER_MESSAGE_SOURCES)
xml = xml.dom.minidom.parseString(OUTPUT)
pretty_xml_as_string = xml.toprettyxml()

print pretty_xml_as_string

# pprint(LINTER_MESSAGES)

# <testsuite tests="3">
#     <testcase classname="foo" name="ASuccessfulTest"/>
#     <testcase classname="foo" name="AnotherSuccessfulTest"/>
#     <testcase classname="foo" name="AFailingTest">
#         <failure type="NotEnoughFoo"> details about failure </failure>
#     </testcase>
# </testsuite>

# <?xml version="1.0" encoding="UTF-8"?>
# <testsuites disabled="" errors="" failures="" name="" tests="" time="">
#     <testsuite disabled="" errors="" failures="" hostname="" id=""
#         name="" package="" skipped="" tests="" time="" timestamp="">
#         <properties>
#             <property name="" value=""/>
#             <property name="" value=""/>
#         </properties>
#         <testcase assertions="" classname="" name="" status="" time="">
#             <skipped/>
#             <error message="" type=""/>
#             <error message="" type=""/>
#             <failure message="" type=""/>
#             <failure message="" type=""/>
#             <system-out/>
#             <system-out/>
#             <system-err/>
#             <system-err/>
#         </testcase>
#         <testcase assertions="" classname="" name="" status="" time="">
#             <skipped/>
#             <error message="" type=""/>
#             <error message="" type=""/>
#             <failure message="" type=""/>
#             <failure message="" type=""/>
#             <system-out/>
#             <system-out/>
#             <system-err/>
#             <system-err/>
#         </testcase>
#         <system-out/>
#         <system-err/>
#     </testsuite>
#     <testsuite disabled="" errors="" failures="" hostname="" id=""
#         name="" package="" skipped="" tests="" time="" timestamp="">
#         <properties>
#             <property name="" value=""/>
#             <property name="" value=""/>
#         </properties>
#         <testcase assertions="" classname="" name="" status="" time="">
#             <skipped/>
#             <error message="" type=""/>
#             <error message="" type=""/>
#             <failure message="" type=""/>
#             <failure message="" type=""/>
#             <system-out/>
#             <system-out/>
#             <system-err/>
#             <system-err/>
#         </testcase>
#         <testcase assertions="" classname="" name="" status="" time="">
#             <skipped/>
#             <error message="" type=""/>
#             <error message="" type=""/>
#             <failure message="" type=""/>
#             <failure message="" type=""/>
#             <system-out/>
#             <system-out/>
#             <system-err/>
#             <system-err/>
#         </testcase>
#         <system-out/>
#         <system-err/>
#     </testsuite>
# </testsuites>
