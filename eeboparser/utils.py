import json
import sys

def get_xml_content(i, fname):
    content = ""
    with open(fname, encoding="utf8", mode='r') as infile:
        content = infile.read()
    d = {}
    d["_id"] = i
    d["xml"] = content
    return d

def estimate_size(dictionary):
    return (sys.getsizeof(json.dumps(dictionary).encode('utf8')) / 1000000)
