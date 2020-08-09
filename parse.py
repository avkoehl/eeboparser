import re
import xml.etree.ElementTree as ET
from joblib import Parallel, delayed
from pathlib import Path

def inter_word_tags_preprocess(raw):
    """ remove tags occuring within a word using re """
    return(re.sub('<SUP>|</SUP>|<SEG>|<SEG [A-Z]*?=.*?">|</SEG>', "", raw))


def handle_gaps(root):
    for g in root.iter('GAP'):
        if g.get("EXTENT") == "1 letter" : g.text = "*"
        if g.get("EXTENT") == "2 letters" : g.text = "**"
    return(root)

def get_text_content(eebo):
    content = ""
    for t in eebo.iter("TEXT"):
        content += " ".join(t.itertext())

    # since they got needlessely delimited in " ".join(t.itertext()
    content = content.replace(" * ", "*")
    content = content.replace(" ** ", "**")

    # not removing non standard characters

    content = " ".join(content.split())

    return(content)

def parse_xml(fname):
    with open(fname, encoding='utf8') as infile:
        root = ET.fromstring (
                inter_word_tags_preprocess(infile.read())
                )

        root = handle_gaps(root)
        content = get_text_content(root.find("EEBO"))
        return(content)


Path('../data/extracted_text/').mkdir(parents=True, exist_ok=True)
p = Path("../data/")
xfiles = list(p.glob('**/*.xml'))

texts = Parallel(n_jobs=4)(delayed(parse_xml)(fname) for fname in xfiles[0:20])
for i in range(0, len(texts)):
    with open("../data/extracted_text/" + xfiles[i].stem + ".txt", 
            encoding="utf-8",
            mode="w") as ofile:
        ofile.write(texts[i])
