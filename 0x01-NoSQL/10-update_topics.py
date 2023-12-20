#!/usr/bin/env python3
"""Defines one function"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Update documents in mongo_collection named 'name'
        with topics key and 'topics' value
        params: mongo_collection - relevant collection
                name - target document 'name' value
                topics - new value for topics key
        return: None
    """
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
