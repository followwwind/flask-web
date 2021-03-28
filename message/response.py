# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  20:57
@desc: json对象
"""
from message.http_code import get_result
from message.decorator import make_decorator


# json对象
class JsonResult(object):

    @staticmethod
    @make_decorator
    def success(data):
        return get_result(200, None, data), 200

    @staticmethod
    @make_decorator
    def result(code, msg, data):
        return get_result(code, msg, data), 200




