import json
import re
import sys

PUNCT_RE = r'[\[\]\|!"#$%&\'()*+,./:;<>?@\^_`{|}~]'

def get_xml_content(i, fname):
    """ get the raw content from a file while saving file name """
    content = ""
    with open(fname, encoding="utf8", mode='r') as infile:
        content = infile.read()
    d = {}
    d["_id"] = i
    d["xml"] = content
    return d

def estimate_size(dictionary):
    """ estimate memory size of a dictionary saved as a string in megabytes """
    return (sys.getsizeof(json.dumps(dictionary).encode('utf8')) / 1000000)

def normalize_text(text):
    """ lowercase, remove digits and punctuation, fix whitespace """
    text = text.lower()
    text = re.sub(r'\d+', '', text) # remove digits
    text = re.sub(PUNCT_RE, '', text) # remove common punctuation (keeps -)
    text = " ".join(text.split()) # normalize whitespace
    return text

def is_roman(term):
    """ return true if the term is a roman numeral """

    # remove alphanumeric
    term = re.sub('[^a-zA-Z ]+', '', term)

    # set to uppercase
    term = term.upper()

    # check if roman numeral
    if re.match('^[MDCLXVI]+$', term) is None:
        return False
    else:
        return True


