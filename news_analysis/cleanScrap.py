# -*- coding: utf-8 -*-
from base64 import encode
import json
import sys
from pkgutil import simplegeneric

@simplegeneric
def get_items(obj):
    while False: # no items, a scalar object
        yield None

@get_items.register(dict)
def _(obj):
    return obj.items() # json object. Edit: iteritems() was removed in Python 3

@get_items.register(list)
def _(obj):
    return enumerate(obj) # json array

def strip_whitespace(json_data):
    for key, value in get_items(json_data):
        if hasattr(value, 'strip'): # json string
            json_data[key] = value.strip()
        else:
            strip_whitespace(value) # recursive call

js=open("scrap_data1.json","rb")
jsCl=open("scrap_data1Clean.json",'w',encoding='utf-8')
data = json.load(js) # read json data from standard input
strip_whitespace(data)

json.dump(data,jsCl, indent=2,ensure_ascii=False)