# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  21:03
@desc: request请求
"""
import flask_restful
from message.http_code import get_result
from flask_restful import abort


# json body请求
def get_json():
    body = flask_restful.request.json
    if body:
        return body
    abort(400, **get_result(code=400, msg='缺少请求数据'))


# get请求
def get_arg(key, default=None):
    value = flask_restful.request.args.get(key, default)
    if value is not None:
        return value
    abort(400, **get_result(code=400, msg='缺少请求参数%s' % key))


# form请求
def get_form(key, default=None):
    value = flask_restful.request.form.get(key, default)
    if value is not None:
        return value
    abort(400, **get_result(code=400, msg='缺少请求参数%s' % key))
