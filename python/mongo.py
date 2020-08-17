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

def insert_metadata(mydb, metadata_list):
    mydb["docs.metadata"].insert_many(metadata_list)

def insert_content(mydb, content_list, truncated_content_list):
    large_content_list = []
    # iterate through content list, moving documents that are too large into another list

    # insert the large documents using grid fs

    # finally insert the two lists (truncated and remaining content_list items
    mydb["docs"].insert_many(content_list)
    mydb["docs.truncated"].insert_many(truncated_content_list)
