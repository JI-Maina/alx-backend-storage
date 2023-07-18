#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """lists all documents in a collection"""

    mongo_collection.find()

    if mongo_collection.count_documents({}) <= 0:
        return []

    return mongo_collection.find()
