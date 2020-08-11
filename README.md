# Repo for the Quintessence Corpus

General workflow:

TBD:edit mongo-credentials.json
run corpus.py 
run adorn.sh

# Setup

need java8+ installed
need python3 requirements from requirements.txt file (pip install --user -r requirements.txt)
need mongodb service running

mongo config json file:
```
cat mongo-credentials.json
{
    "database": "quintessence",
    "host": "localhost",
    "port": "27017",
    "user": "",
    "pwd": ""
}
```

# Corpus.py

Takes as input eebo xml files, parses those files for the text content and metadata. 

TBD:
Stores the results into the mongodb database.

# Adorn.sh
TBD:
Runs a java command line program that connects to the mongo database, iterates through the texts and uses morphadorner to adorn them. Then saves the results back into the mongo database.
