# Repo for the Quintessence Corpus

This repo contains a python package and some java code for processing the EEBO-TCP files given to us by Anupam.

# Setup

To run on the full eebo corpus, you need probably 20GB of memory as it stores the whole corpus in RAM.

need java8+ installed  
need poetry installed
need mongodb installed

poetry build && poetry install

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

# 1_parse_xml.py

Takes as input eebo xml files, parses those files for the text content and metadata. 

Stores the results into the mongodb database.

# 2_adorn.sh

bash script that calls the java code that reads in text extracted from the xml files with 1_parse_xml.py, writes adorned output directory to mongodb

