# -*- coding: utf-8 -*-
"""
Created on Wed May 24 01:29:37 2017

@author: Admin-pc
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "ahmedabad_india.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons","Temple"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Ave" : "Avenue",
            "Ave." : "Avenue",
            "Rd" : "Road",
            "Rd." : "Road",
            "Blvd" : "Boulevard",
            "Blvd." : "Boulevard",
            "Cir" : "Circle",
            "Cir." : "Circle",
            "Ct" : "Court",
            "Ct." : "Court",
            "Dr" : "Drive",
            "Dr." : "Drive",
            "Pl" : "Place",
            "Pl." : "Place",
            "road":"Road",
            "ROAD":"Road",
            "orad":"Road",
            "rasta":"Road",
            "Roads":"Road",
            "marg":"Road",
            "Marg":"Road",
            "bridge":"Bridge",
            "gandhi":"Gandhi",
            "Mandir":"Temple"
            
            }



def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    #print tag.attrib['v']
                    audit_street_type(street_types, tag.attrib['v'])
                    
    osm_file.close()
    return street_types


def update_name(name, mapping):

    # YOUR CODE HERE

    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        print street_type
        if street_type in mapping.keys():
            print 'Before: ' , name
            if m not in expected:
                name = re.sub(m.group(), mapping[m.group()], name)
                print 'After: ', name
    #return name

    return name


def test():
    st_types = audit(OSMFILE)
   
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name


if __name__ == '__main__':
    test()