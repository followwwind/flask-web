# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:24
@desc:
"""

from flask_restful import abort
from message.decorator import make_decorator, Response
from message.http_code import get_result
from models.user import UserModel


class UserOperation(object):

    @staticmethod
    @make_decorator
    def reg(user):
        username = user.get('username', '')
        password = user.get('password', '')
        u = UserModel.get_by_name(username)
        if u:
            abort(500, **get_result(code=500, msg='该用户已存在'))
        UserModel.insert(username, password)
        return Response(data={})

    @staticmethod
    @make_decorator
    def login(user):
        username = user.get('username', '')
        password = user.get('password', '')
        u = UserModel.get_by_name(username)
        if not u:
            abort(500, **get_result(code=500, msg='账号或密码错误'))
        if password != u['password']:
            abort(500, **get_result(code=500, msg='账号或密码错误'))
        return Response(data=u)

    @staticmethod
    @make_decorator
    def bind_assert(user):
        _id = user.get('_id', '')
        assert_id = user.get('assert_id', '')
        UserModel.bind_assert(_id, assert_id)
        return Response(data={})
