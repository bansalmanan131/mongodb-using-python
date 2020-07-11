import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://bansalmanan131:BANSALMANAN!#!@cluster0.fdg3i.gcp.mongodb.net/test?retryWrites=true&w=majority")
db=cluster["test"]
collection=db["testcase"]

post={"_id":1, "name":"jim", "score":6}

collection.insert_one(post)