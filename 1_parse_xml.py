""" Main script to parse the xml and store the text and metadata in a database

    usage: poetry run python 1_parse_xml.py

    Arguments to main:
    db - if True save outputs to database)
    input_dir - root directory of all xml files, will be searched recursively
    ncores - number of cores to use to parse the xml files with
"""
from pathlib import Path
import sys
import json

from joblib import Parallel, delayed
import pymongo

from eeboparser import clean_meta
from eeboparser import mongo
from eeboparser import parse_xml
from eeboparser import utils


def main(db=False, input_dir = "../data/", ncores=4):

    print("reading in xml documents")
    files = list(Path(input_dir).glob('**/*.xml'))
    xml = [utils.get_xml_content(i, fname) for i, fname in enumerate(files[0:500])]
    
    print("parsing xml")
    results = Parallel(n_jobs=ncores)(delayed(parse_xml.parse_xml)(x["_id"], 
        x["xml"]) for x in xml)
    meta, texts,truncated = zip(*results)
    
    # clean meta
    
    if db:
        print("connecting to mongo database")
        mydb = mongo.open_db_connection("mongo-credentials.json")
        for col in ["docs.xml", "docs.xml.chunks", "docs.xml.files", 
                "docs.meta", "docs.text", "docs.truncated"]:
            mydb[col].drop()

        print("write to database")
        mongo.insert_xml_gridfs(mydb, "docs.xml", xml)
        r = mydb["docs.meta"].insert_many(meta)
        r = mydb["docs.truncated"].insert_many(truncated)
        r = mydb["docs.text"].insert_many(texts)

if __name__ == "__main__":
    main()
