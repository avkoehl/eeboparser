from pathlib import Path
import sys

from joblib import Parallel, delayed
import json

import python.parse_xml as px
import python.mongo as m

print("connecting to mongo database")
mydb = m.open_db_connection("mongo-credentials.json")

print("reading in xml documents")
xml = []
files = list(Path("../data/").glob('**/*.xml'))
for f in files:
    xml.append(f.read())

print("write to database")


print("parsing xml")
results = Parallel(n_jobs=20)(delayed(px.parse_xml)(f) for f in files[1:10000])

print("inserting into database")
metadata_list = []
content_list = []
truncated_content_list = []
large_content_list = []
for i,result in enumerate(results):
    result[0]["_id"] = i
    content = {"_id": i,
               "raw": result[1]}
    truncated = {"_id": i,
                 "raw": result[1][0:500]}

    #print(len(json.dumps(content)) / 1000000)
    size_estimate = sys.getsizeof(json.dumps(content).encode('utf8')) / 1000000
    if (size_estimate > 4):
        print(i, size_estimate)


    metadata_list.append(result[0])
    content_list.append(content)
    truncated_content_list.append(truncated)


#m.insert_metadata(mydb, metadata_list)
#m.insert_content(mydb, content_list, truncated_content_list)
#m.insert_large_content(mydb, large_content_list)
