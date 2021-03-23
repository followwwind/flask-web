# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  21:10
@desc:
"""
from flask_restplus.resource import Resource
from config import api
from message.decorator import Response
from message.response import JsonResult


class Hello(Resource):

    @staticmethod
    @JsonResult.success(result=dict)
    def get():
        result = {
            'name': 'hello world'
        }
        return Response(result=result)


ns = api.namespace('api/hello', 'hello')
ns.add_resource(Hello, '/')
