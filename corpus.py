from pathlib import Path

from joblib import Parallel, delayed

import python.parse_xml as px

Path('../data/extracted_text/').mkdir(parents=True, exist_ok=True)
p = Path("../data/")
files = list(p.glob('**/*.xml'))

results = [px.parse_xml(fname) for fname in files[0:20]]

#results = Parallel(n_jobs=4)(delayed(parse_xml)(f) for f in files[0:2000])
#for i in range(0, len(results)):
#    with open("../data/extracted_text/" + files[i].stem + ".txt", 
#            encoding="utf-8",
#            mode="w") as ofile:
#        ofile.write(results[i][1])
