# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:24
@desc:
"""

from flask_restful import abort
from message.decorator import make_decorator, Response
from message.http_code import get_result
from models.account import AccountModel


class AccountOperation(object):

    @staticmethod
    @make_decorator
    def insert(account):
        if not account:
            abort(400, **get_result(code=400, msg='参数错误'))
        AccountModel.insert(account)
        return Response(data={})

    @staticmethod
    @make_decorator
    def delete(account):
        if not account:
            abort(400, **get_result(code=400, msg='参数错误'))
        AccountModel.delete(account)
        return Response(data={})

    @staticmethod
    @make_decorator
    def list(account, page_num, page_size):
        if not account:
            abort(400, **get_result(code=400, msg='参数错误'))
        page = AccountModel.list(account, page_num, page_size)
        return Response(data=page)

    @staticmethod
    @make_decorator
    def update(account):
        if not account:
            abort(400, **get_result(code=400, msg='参数错误'))
        AccountModel.update(account)
        return Response(data={})
