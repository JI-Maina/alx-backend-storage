#!/usr/bin/env python3
"""
A Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

client = MongoClient()

db = client.logs

res = db.nginx.count_documents({})
get = db.nginx.count_documents({'method': 'GET'})
post = db.nginx.count_documents({'method': 'POST'})
put = db.nginx.count_documents({'method': 'PUT'})
patch = db.nginx.count_documents({'method': 'PATCH'})
delet = db.nginx.count_documents({'method': 'DELETE'})
path = db.nginx.count_documents({'method': 'GET', 'path': '/status'})


print("{} logs".format(res))
print("Methods:")
print("\tmethod GET: {}".format(get))
print("\tmethod POST: {}".format(post))
print("\tmethod PUT: {}".format(put))
print("\tmethod PATCH: {}".format(patch))
print("\tmethod DELETE: {}".format(delet))
print("{} status check".format(path))
