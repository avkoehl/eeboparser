# Repo for the Quintessence Corpus

General workflow:

edit mongo-credentials.json  
run corpus.py   

# Setup

need java8+ installed  
need python3 requirements from requirements.txt file (pip install --user -r requirements.txt)  
need mongodb service running  

mongo config json file:
```
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

Stores the results into the mongodb database.

# Adorn

navigate to java directory
ant run

