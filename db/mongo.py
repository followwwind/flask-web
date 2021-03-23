# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  22:23
@desc: mongodb client
"""
import pymongo


class MongoClient(object):

    def __init__(self, host, port, db, user=None, password=None):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.conn = pymongo.MongoClient(host=self.host, port=self.port, serverSelectionTimeoutMS=10000)
        if self.user and self.password:
            db_auth = self.conn[self.db]
            db_auth.authenticate(self.user, self.password)

    def get_collection(self, collection):
        """获取集合"""
        collection = self.conn[self.db][collection]
        return collection

    def get_all_collection(self):
        """获取集合"""
        collections = self.conn[self.db].list_collection_names()
        return collections


if __name__ == '__main__':
    opts = {
        "host": "118.193.37.106",
        "port": "27017",
        "db": "",
        "user": "user1",
        "password": "789789"
    }
    client = MongoClient(**opts)
    all_collection = client.get_all_collection()
    print(all_collection)
