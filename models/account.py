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
        db.delete_one('account', account)
        return Response({})

    @staticmethod
    def list(account, page_num, page_size):
        total_count = db.query_count('account', account)
        if page_num <= 0:
            page_num = 1
        offset = (page_num - 1) * page_size
        data_list = db.query_search_page('account', account, page_size, offset)
        data_arr = []
        for i in range(0, len(data_list)):
            data_arr.append({
                '_id': str(data_list[i]['_id']),
                'exchange': data_list[i]['exchange'],
                'desc': data_list[i]['desc'],
                'key': data_list[i]['key'],
                'secret': data_list[i]['secret'],
                'userId': data_list[i]['user_id'],
            })
        return Response(total=total_count, data=data_arr, pageNum=page_num, pageSize=page_size)
