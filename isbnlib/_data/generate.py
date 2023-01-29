#!/usr/bin/env python3

import requests
from datetime import datetime, timezone
from xml.dom import minidom

RANGEFILEURL = 'https://www.isbn-international.org/export_rangemessage.xml'
M_DATE_FMT = '%a, %d %b %Y %H:%M:%S %Z'
MASKFILE = 'data4mask.py'
INFOFILE = 'data4info.py'


HEADER = """# flake8:noqa
# pylint:skip-file
# isort:skip_file
# fmt:off
# Produced by 'generate.py'@'{generatetime}'

#                   WARNING
# THIS FILE WAS PRODUCED BY TOOLS THAT AUTOMATICALLY
# GATHER THE RELEVANT INFORMATION FROM SEVERAL SOURCES
#            DON'T EDIT IT MANUALLY!

"""


MASKBODY = """
ranges={ranges}
RDDATE='{rddate}'
"""


INFOBODY = """
countries={countries}
identifiers={identifiers}
RDDATE='{rddate}'
"""


def ruletriples(node):
    rules = [] 
    for rule in node:
        start, end = rule.getElementsByTagName('Range')[0].firstChild.nodeValue.split('-')
        length = rule.getElementsByTagName('Length')[0].firstChild.nodeValue
        rules.append(tuple(map(int, [start, end, length])))
    return tuple(rules)


def group_identifiers(identifiers):
    """Group indentifier prefixes by length."""
    groups = {}
    for k in identifiers:
        _, group = k.split('-')
        if len(group) in groups:
            groups[len(group)].append(k)
        else:
            groups[len(group)] = [k]
    keys = list(groups.keys())
    keys.sort()
    return tuple([tuple(groups[k]) for k in keys])


def clean(s, style='mask'):
    """Perform formatting to match isbntools-dev ouput."""
    # This isn't strictly necessary, but makes it easy to diff the output
    s = s.replace("', '", "','").replace('), (', '),(')
    if style == 'info':
        s = s.replace("': '", "':'")
    return s


def main():
    generatetime = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    r = requests.get(RANGEFILEURL)
    dom = minidom.parseString(r.text)
    #dom = minidom.parse('RangeMessage.xml')
    nodes = dom.getElementsByTagName('Group')
    messagedate = dom.getElementsByTagName('MessageDate')[0]
    rddate = datetime.strptime(messagedate.firstChild.nodeValue, M_DATE_FMT)
    rddate = datetime.strftime(rddate, '%Y%m%d')
    ranges = {}
    countries = {}
    for node in nodes:
        prefix = node.getElementsByTagName('Prefix')[0].firstChild.nodeValue
        agency = node.getElementsByTagName('Agency')[0].firstChild.nodeValue
        rules = node.getElementsByTagName('Rule')
        ranges[prefix] = ruletriples(rules)
        countries[prefix] = agency

    identifiers = group_identifiers(countries.keys())

    data = {
        'generatetime': generatetime,
        'ranges': ranges,
        'countries': countries,
        'identifiers': identifiers,
        'rddate': rddate}

    maskdata = clean((HEADER + MASKBODY).format(**data), 'mask')
    infodata = clean((HEADER + INFOBODY).format(**data), 'info')

    with open(MASKFILE, 'w') as mask:
        mask.write(maskdata)

    with open(INFOFILE, 'w') as info:
        info.write(infodata)


if __name__ == '__main__':
    main()
