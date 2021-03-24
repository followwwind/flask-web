# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:25
@desc:
"""

from config import db
from message.decorator import Response


class AccountModel(object):

    @staticmethod
    def insert(account):
        _id = db.insert_one('account', account)
        return Response(_id=_id)

    @staticmethod
    def update(account):
        doc = db.update('account', account)
        if not doc:
            return Response({})
        return Response(_id=doc['_id'])

    @staticmethod
    def delete(account):
        doc = db.remove('account', account)
        if not doc:
            return Response({})
        return Response(_id=doc['_id'])

    @staticmethod
    def list(account, page_num, page_size):
        total_count = db.query_count('account', account)
        data_list = db.query_search_page('account', account, page_num, page_size)
        return Response(total=total_count, data=data_list, pageNum=page_num, pageSize=page_size)
