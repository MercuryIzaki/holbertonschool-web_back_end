#!/usr/bin/env python3
"""
Module that provides a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a mongo_collection
    Returns an empty list if no document in the collection
    """
    return list(mongo_collection.find())
