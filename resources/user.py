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
from operations.user import UserOperation


class User(Resource):

    @staticmethod
    @JsonResult.success(data=dict)
    @UserOperation.reg(user=dict)
    def put():
        json = get_json()
        user = {
            'username': json.get('username', ''),
            'password': json.get('password', '')
        }
        return Response(user=user)

    @staticmethod
    @JsonResult.success(data=dict)
    @UserOperation.login(user=dict)
    def post():
        json = get_json()
        user = {
            'username': json.get('username', ''),
            'password': json.get('password', '')
        }
        return Response(user=user)


class UserAssert(Resource):

    @staticmethod
    @JsonResult.success(data=dict)
    @UserOperation.bind_assert(user=dict)
    def post():
        json = get_json()
        _id = json.get('_id', '')
        if _id == '':
            abort(400, **get_result(code=400, msg='参数错误'))
        user = {
            '_id': _id,
            'assert_id': json.get('assert_id', '')
        }
        return Response(user=user)


ns = api.namespace('api/user', 'user')
ns.add_resource(User, '/')
ns.add_resource(UserAssert, '/assert')
