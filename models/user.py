# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:24
@desc:
"""

from config import db
from message.decorator import Response


class UserModel(object):

    @staticmethod
    def insert(username, password):
        user = {
            'username': username,
            'password': password,
            'real_value_all': 0.00,
            'profit': 0.00,
            'profit_pct': 0.00
        }
        db.insert_one('user', user)

    @staticmethod
    def bind_assert(_id, assert_id):
        user = {
            '_id': _id,
            'assert_id': assert_id
        }
        db.update('user', user)

    @staticmethod
    def get_by_name(username):
        user = {
            'username': username
        }
        doc = db.query_one('user', user)
        if not doc:
            return Response({})
        return Response(_id=str(doc['_id']), username=doc['username'], password=doc['password'],
                        realValueAll=doc['real_value_all'], profit=doc['profit'], profitPct=doc['profit_pct'])
