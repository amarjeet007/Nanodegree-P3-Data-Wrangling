# -*- coding: utf-8 -*-
"""
Created on Tue May 23 22:34:32 2017

@author: Admin-pc
"""

import xml.etree.cElementTree as ET
import pprint


OSMFILE = "ahmedabad_india.osm"

def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags: 
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags
    
pprint.pprint(count_tags(OSMFILE))