import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URI"))
DB = client["viajaTechDatabase"]
