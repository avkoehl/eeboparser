import time
from pathlib import Path

from joblib import Parallel, delayed

import python.parse_xml as px

Path('../data/extracted_text/').mkdir(parents=True, exist_ok=True)
p = Path("../data/")
files = list(p.glob('**/*.xml'))


print("running on all files 4 cores")
start = time.time()
results = Parallel(n_jobs=4)(delayed(px.parse_xml)(f) for f in files)
for i in range(0, len(results)):
    with open("../data/extracted_text/" + files[i].stem + ".txt", 
            encoding="utf-8",
            mode="w") as ofile:
        ofile.write(results[i][1])

print("elapsed time: ", time.time() - start, " seconds")
