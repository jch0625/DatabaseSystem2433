import pymongo
from pymongo import MongoClient
import certifi
import datetime



    # Provide the mongodb atlas url to connect python to mongodb using pymongo
client = MongoClient( "mongodb+srv://dbms:jchjchjch@dbns.swthwi3.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = certifi.where())

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
db = client["dbmsfinal"]
collection = db["dbms"]
collection.insert_one({"_id":0, "user_name":"Soumi"})
collection.insert_one({"_id":100, "user_name":"Ravi"})

# Create the database for our example (we will use the same database throughout the tutorial




# This is added so that many files can reuse the function get_database()

# myclient = pymongo.MongoClient("mongodb+srv://dbms:jchjchjch@dbns.swthwi3.mongodb.net/?retryWrites=true&w=majority")
# mydb = myclient["dbns"]
# mycol = mydb["dbmsfinal"]
# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
