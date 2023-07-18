#!/usr/bin/env python3
"""
Defines a Python function that returns list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""

    res = mongo_collection.find({'topics': {'$eq': topic}})

    return res
