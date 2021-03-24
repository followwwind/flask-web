# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:24
@desc:
"""
from flask_restful import abort
from flask_restplus.resource import Resource
from config import api
from message.decorator import Response
from message.http_code import get_result
from message.response import JsonResult
from message.request import get_json
from operations.account import AccountOperation


class User(Resource):

    @staticmethod
    @JsonResult.success(data=dict)
    @AccountOperation.list(account=dict, page_num=int, page_size=int)
    def get():
        json = get_json()
        query = {
            'exchange': json.get('exchange', '')
        }
        page_num = int(json.get('pageNum', 1))
        page_size = int(json.get('pageSize', 1))
        return Response(account=query, page_num=page_num, page_size=page_size)

    @staticmethod
    @JsonResult.success(data=dict)
    @AccountOperation.update(account=dict)
    def put():
        json = get_json()
        _id = json.get('_id', '')
        if _id == '':
            abort(400, **get_result(code=400, msg='参数错误'))
        account = {
            '_id': _id,
            'exchange': json.get('exchange', ''),
            'desc': json.get('desc', ''),
            'key': json.get('key', ''),
            'secret': json.get('secret', ''),
            'user_id': json.get('userId', '')
        }
        return Response(account=account)

    @staticmethod
    @JsonResult.success(data=dict)
    @AccountOperation.insert(account=dict)
    def post():
        json = get_json()
        account = {
            'exchange': json.get('exchange', ''),
            'desc': json.get('desc', ''),
            'key': json.get('key', ''),
            'secret': json.get('secret', ''),
            'user_id': json.get('userId', '')
        }
        return Response(account=account)

    @staticmethod
    @JsonResult.success(data=dict)
    @AccountOperation.delete(account=dict)
    def delete():
        json = get_json()
        _id = json.get('_id', '')
        if _id == '':
            abort(400, **get_result(code=400, msg='参数错误'))
        account = {
            '_id': _id
        }
        return Response(account=account)


ns = api.namespace('api/account', 'account')
ns.add_resource(User, '/')
