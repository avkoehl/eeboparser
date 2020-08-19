from sys import exit
import json

import pymongo
import gridfs as gd

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
    return (mydb)

def insert_xml_gridfs(db, collection_name, dict_list):
    fs = gd.GridFS(db, collection_name)
    for d in dict_list:
        fs.put(bytes(d["xml"], encoding="utf8"), _id = d["_id"])
    return 

