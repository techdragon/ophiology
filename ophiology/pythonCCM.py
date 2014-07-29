import json
# from pprint import pprint
import os, fnmatch
# import xml.etree.ElementTree as ET
# import xml.dom.minidom

import envoy

def recursive_path_split(path):
    """ taken from stack overflow
    http://stackoverflow.com/questions/13505819/python-split-path-recursively
    """
    rest, tail = os.path.split(path)
    if rest == '':
        return tail,
    return recursive_path_split(rest) + (tail,)

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                # filename = os.path.join(root, basename)
                filename = os.path.relpath(os.path.join(root, basename), directory)
                yield filename

def build_function_metric(metrics, filename, metric_data):
    """TODO: Docstring"""
    # print "Function Metric"
    pathbits = recursive_path_split(filename)
    pypath = ('.'.join(pathbits))[:-3]
    if pypath[-8:] == '__init__':
        pypath = pypath[:-9]
    unit = (
        pypath +
        '::' +
        metric_data['name']
    )
        # metric_data['type'] +
    # classification = metric_data['classification']

    classification = metric_data['rank']
    xml = build_metric_xml(
        complexity=metric_data['complexity'],
        unit=unit,
        classification=classification,
        file=filename,
        startLineNumber=metric_data['lineno'],
        endLineNumber=metric_data['endline'],
        )
    print xml
    metrics.append(xml)

def build_method_metric(metrics, filename, metric_data):
    """TODO: Docstring"""
    # print "Method Metric"
    pathbits = recursive_path_split(filename)
    pypath = ('.'.join(pathbits))[:-3]
    if pypath[-8:] == '__init__':
        pypath = pypath[:-9]
    unit = (
        pypath +
        '::' +
        metric_data['name']
    )
        # metric_data['type'] +
    # classification = metric_data['classification']

    classification = metric_data['rank']
    xml = build_metric_xml(
        complexity=metric_data['complexity'],
        unit=unit,
        classification=classification,
        file=filename,
        startLineNumber=metric_data['lineno'],
        endLineNumber=metric_data['endline'],
        )
    # print xml
    metrics.append(xml)
    # pass

def build_class_metric(metrics, filename, metric_data):
    """TODO: Docstring"""
    # print "Class Metric"
    pathbits = recursive_path_split(filename)
    pypath = ('.'.join(pathbits))[:-3]
    if pypath[-8:] == '__init__':
        pypath = pypath[:-9]
    unit = (
        pypath +
        '::' +
        metric_data['name']
    )
        # metric_data['type'] +
    # classification = metric_data['classification']

    classification = metric_data['rank']
    xml = build_metric_xml(
        complexity=metric_data['complexity'],
        unit=unit,
        classification=classification,
        file=filename,
        startLineNumber=metric_data['lineno'],
        endLineNumber=metric_data['endline'],
        )
    # print xml
    metrics.append(xml)

    if metric_data['methods']:
        for k in metric_data['methods']:
            build_classmethod_metric(
                metrics=metrics,
                filename=filename,
                metric_data=k,
                classname=metric_data['name']
                )

    # pass

def build_classmethod_metric(metrics, filename, metric_data, classname):
    """TODO: Docstring"""
    # print "ClassMethod Metric"
    pathbits = recursive_path_split(filename)
    pypath = ('.'.join(pathbits))[:-3]
    if pypath[-8:] == '__init__':
        pypath = pypath[:-9]
    unit = (
        pypath +
        '::' +
        classname + '.' + metric_data['name']
    )

    classification = metric_data['rank']
    xml = build_metric_xml(
        complexity=metric_data['complexity'],
        unit=unit,
        classification=classification,
        file=filename,
        startLineNumber=metric_data['lineno'],
        endLineNumber=metric_data['endline'],
        )
    print xml
    metrics.append(xml)
    # pass


def build_metric_xml(**kwds):
    """TODO: Docstring"""
    try:
        pypath = os.path
        sloc = kwds['endLineNumber'] - kwds['startLineNumber']
        return '\n'.join([
            '<metric>',
            '  <complexity>%s</complexity>' % kwds['complexity'],
            '  <unit>%s</unit>' % kwds['unit'],
            '  <classification>%s</classification>' % kwds['classification'],
            '  <file>%s</file>' % kwds['file'],
            '  <startLineNumber>%s</startLineNumber>' % kwds['startLineNumber'],
            '  <endLineNumber>%s</endLineNumber>' % kwds['endLineNumber'],
            '  <SLOC>%s</SLOC>' % sloc,
            '</metric>'
        ])
    except:
        raise

# metrics = []


def execute():
    # command = 'radon cc -s --json %s' % 'os.getcwd()'
    command = 'radon cc -s --json %s' % '.'
    cmd = envoy.run(command)
    # print cmd.std_out
    json_data = cmd.std_out
        # for n in iter(cmd.std_out.splitlines()):
        #     metrics.append(n)

    data = json.loads(json_data)
    # pprint(data)

    filenames = set()
    metrics = []

    for key, value in data.iteritems():
        filenames.add(key)

    for i in xrange(len(filenames)):
        filename = filenames.pop()
        # print filename
        for index, j in enumerate(data[filename]):
            # print j['type']
            # print j
            if j['type'] == 'function':
                build_function_metric(
                    metrics=metrics, filename=filename, metric_data=j)
            if j['type'] == 'class':
                build_class_metric(
                    metrics=metrics, filename=filename, metric_data=j)
            if j['type'] == 'method':
                build_method_metric(
                    metrics=metrics, filename=filename, metric_data=j)

    f = open('ccm.xml', 'w')
    for metric in metrics:
        f.write(metric)
    f.close()
