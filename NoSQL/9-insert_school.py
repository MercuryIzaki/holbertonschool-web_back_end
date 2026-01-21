#!/usr/bin/env python3
"""
Module that provides a function to insert a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    Returns the new _id
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
