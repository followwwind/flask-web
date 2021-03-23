# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  20:58
@desc: http请求状态码
"""

# http请求状态码
HTTP_CODE = {
    200: '成功',
    400: '参数错误',
    403: '请求被拒绝',
    404: '未找到资源',
    500: '服务器内部错误'
}


def get_result(code, msg=None, data=None):
    return {'code': code, 'msg': msg if msg else HTTP_CODE[code], 'data': data}
