# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:24
@desc:
"""

from flask_restful import abort
from message.decorator import make_decorator, Response
from message.http_code import get_result
from models.assert_info import AssertInfoModel


class AssertOperation(object):

    @staticmethod
    @make_decorator
    def insert(assert_info):
        if not assert_info:
            abort(400, **get_result(code=400, msg='参数错误'))
        AssertInfoModel.insert(assert_info)
        return Response(data={})

    @staticmethod
    @make_decorator
    def delete(assert_info):
        if not assert_info:
            abort(400, **get_result(code=400, msg='参数错误'))
        AssertInfoModel.delete(assert_info)
        return Response(data={})

    @staticmethod
    @make_decorator
    def get(assert_info):
        if not assert_info:
            abort(400, **get_result(code=400, msg='参数错误'))
        doc = AssertInfoModel.get(assert_info)
        return Response(data=doc)

    @staticmethod
    @make_decorator
    def list(assert_info, page_num, page_size):
        page = AssertInfoModel.list(assert_info, page_num, page_size)
        return Response(data=page)

    @staticmethod
    @make_decorator
    def line(num, page_num, page_size):
        data = AssertInfoModel.line(num, page_num, page_size)
        return Response(data=data)

    @staticmethod
    @make_decorator
    def update(assert_info):
        if not assert_info:
            abort(400, **get_result(code=400, msg='参数错误'))
        AssertInfoModel.update(assert_info)
        return Response(data={})
