#!/usr/bin/env python3

"""Defines a single function"""
import pymongo


def list_all(mongo_collection):
    """Create a list of documents
        params: mongo_collection - a pymongo collection object
        return: List
    """
    documents = mongo_collection.find()
    return [document for document in documents]
