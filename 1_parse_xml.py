from pathlib import Path
import sys
import json

from joblib import Parallel, delayed
import pymongo

import python.utils as ut
import python.parse_xml as px
import python.mongo as m

print("connecting to mongo database")
mydb = m.open_db_connection("mongo-credentials.json")
mydb["docs.xml"].drop()
mydb["docs.xml.chunks"].drop()
mydb["docs.xml.files"].drop()
mydb["docs.meta"].drop()
mydb["docs.text"].drop()
mydb["docs.truncated"].drop()

print("reading in xml documents")
files = list(Path("../data/").glob('**/*.xml'))
xml = [ut.get_xml_content(i, fname) for i, fname in enumerate(files)]

print("write to database")
m.insert_xml_gridfs(mydb, "docs.xml", xml)

print("parsing xml")
results = Parallel(n_jobs=20)(delayed(px.parse_xml)(x["_id"], x["xml"]) for x in xml)

print("inserting parsed corpus into database")
meta, texts,truncated = zip(*results)
r = mydb["docs.meta"].insert_many(meta)
r = mydb["docs.truncated"].insert_many(truncated)
r = mydb["docs.text"].insert_many(texts)
