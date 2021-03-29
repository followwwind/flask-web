# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  22:23
@desc: mongodb client
"""
import pymongo
from bson import ObjectId


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

    def is_exist(self, collection):
        """判断集合是否存在"""
        collections = self.conn[self.db].list_collection_names()
        return True if collection in collections else False

    def insert_one(self, collection, document):
        """插入一条数据"""
        result = self.get_collection(collection).insert_one(document)
        return result.inserted_id

    def insert(self, collection, document):
        """插入数据"""
        result = self.get_collection(collection).insert(document)
        return result.inserted_id

    def remove(self, collection, document):
        """移除数据"""
        result = self.get_collection(collection).remove(document)
        return result

    def delete_one(self, collection, document):
        """移除数据"""
        result = self.get_collection(collection).delete_one({"_id": ObjectId(document['_id'])})
        return result

    def update(self, collection, document):
        """更新数据"""
        result = self.get_collection(collection).update({"_id": document['_id']}, document)
        return result

    def query_one(self, collection, document):
        """查找数据"""
        result = self.get_collection(collection).find_one(document)
        return result

    def query(self, collection, document):
        """查找数据"""
        result = self.get_collection(collection).find(document)
        return result

    def query_count(self, collection, document):
        """查找总数"""
        result = self.get_collection(collection).find(document).count()
        return result

    def query_search_page(self, collection, document, limit, offset):
        """查找总数"""
        result = list(self.get_collection(collection).find(document).limit(limit).skip(offset))
        return result

    def query_search_page_sort(self, collection, document, limit, offset, sort):
        """查找总数"""
        result = list(self.get_collection(collection).find(document).limit(limit).skip(offset).sort(sort))
        return result


if __name__ == '__main__':
    opts = {
        "host": "localhost",
        "port": 27017,
        "db": "test",
        "user": "test",
        "password": "123456"
    }
    client = MongoClient(**opts)
    all_collection = client.get_all_collection()
    print(all_collection)
