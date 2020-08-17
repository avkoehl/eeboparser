from sys import exit
import pymongo
import json

def load_credentials(fname):
    with open(fname) as cfg:
        data = json.load(cfg)
        return( {
            "database": data["database"],
            "host": data["host"],
            "port": int(data["port"]),
            "user": data["user"],
            "pwd": data["pwd"] })

def open_db_connection(fname, overwrite = True):
    credentials = load_credentials(fname)
    myclient = pymongo.MongoClient(host = credentials["host"],
        port= credentials["port"])

    mydb = myclient[credentials["database"]]

    if credentials["database"] in myclient.list_database_names():
        print("quintessence already exits!")
        if overwrite:
            print("... dropping docs, docs.metadata, docs.truncated")
            mydb["docs.metadata"].drop() 
            mydb["docs"].drop() 
            mydb["docs.truncated"].drop() 
        else:
            print("... exiting")
            exit()
    return (mydb)

# these four are unnecessary in the mongo util script. remove them and just do this stuff from the main executable

# eebo xml as raw utf8 strings
# everything else as arrays of strings
# rewrite parse xml to pull from the database?
# yeah, just load whole thing into memorry parse xml takes in list of strings (full xml file content)
# rename corpus.py to main.py
# insert the xml with main.py
# also call the java jar from the main.py
def insert_xml(mydb, xml
def insert_metadata(mydb, metadata_list):
    mydb["docs.metadata"].insert_many(metadata_list)

def insert_content(mydb, content_list, truncated_content_list):
    mydb["docs"].insert_many(content_list)
    mydb["docs.truncated"].insert_many(truncated_content_list)

#def insert_large_documents(mydb, large_content_list):
