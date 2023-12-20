#!/usr/bin/env python3
"""Defines one function"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert a document into a collection
        params: mongo_collection - pymongo collection object
                kwargs - Dictionary to be made into a document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
