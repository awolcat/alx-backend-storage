#!/usr/bin/env python3
"""A script that gathers/formats stats from a mongodb database"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    r = (
         f"{nginx_collection.count()} logs\n"
         f"Methods:\n"
         f"\tmethod GET: {nginx_collection.find({'method': 'GET'}).count()}\n"
         f"""\tmethod POST: {nginx_collection.find(
                                                 {'method': 'POST'}
                                                 ).count()}\n"""
         f"\tmethod PUT: {nginx_collection.find({'method': 'PUT'}).count()}\n"
         f"""\tmethod PATCH: {nginx_collection.find(
                                                  {'method': 'PATCH'}
                                                  ).count()}\n"""
         f"""\tmethod DELETE: {nginx_collection.find(
                                                   {'method': 'DELETE'}
                                                   ).count()}\n"""
         f"""{nginx_collection.find(
                                  {'$and': [{'method': 'GET'},
                                            {'path': '/status'}]}
                                        ).count()} status check"""
        )
    print(r)
