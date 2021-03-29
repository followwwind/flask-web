# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:24
@desc:
"""
from flask_restplus.resource import Resource
from config import api
from message.decorator import Response
from message.response import JsonResult
from message.request import get_json
from operations.assert_info import AssertOperation


class AssertInfo(Resource):

    @staticmethod
    @JsonResult.success(data=dict)
    @AssertOperation.get(assert_info=dict)
    def get():
        json = get_json()
        assert_info = {
            '_id': json.get('_id', ''),
        }
        return Response(assert_info=assert_info)


class AssertLine(Resource):

    @staticmethod
    @JsonResult.success(data=dict)
    @AssertOperation.line(num=int, page_num=int, page_size=int)
    def post():
        json = get_json()
        page_num = int(json.get('pageNum', 1))
        num = int(json.get('num', 2))
        page_size = int(json.get('pageSize', 10))
        return Response(num=num, page_num=page_num, page_size=page_size)


ns = api.namespace('api/assert', 'assert')
ns.add_resource(AssertInfo, '/')
ns.add_resource(AssertLine, '/line')
