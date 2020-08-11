from pathlib import Path

from joblib import Parallel, delayed

import python.parse_xml as px
import python.mongo as m

print("connecting to mongo database")
mydb = m.open_db_connection("mongo-credentials.json")

print("parsing xml")
files = list(Path("../data/").glob('**/*.xml'))[0:100]
results = Parallel(n_jobs=4)(delayed(px.parse_xml)(f) for f in files)

print("inserting into database")
metadata_list = []
content_list = []
truncated_content_list = []
for i,result in enumerate(results):
    result[0]["_id"] = i
    content = {"_id": i,
               "raw": result[1]}
    truncated = {"_id": i,
                 "raw": result[1][0:500]}
    metadata_list.append(result[0])
    content_list.append(content)
    truncated_content_list.append(truncated)


m.insert_metadata(mydb, metadata_list)
m.insert_content(mydb, content_list, truncated_content_list)
