# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  22:02
@desc: 装饰器
"""
import functools


# 返回对象
class Response(dict):

    def __init__(self, *args, **kwargs):
        super(Response, self).__init__(*args, **kwargs)


# 封装装饰器
def make_decorator(f):
    def input_params(**params):
        restriction = {}
        values = {}
        for name in params:
            type = params[name]
        try:
            isinstance(0, type)
            restriction.update({name: type})
        except:
            values.update({name: type})

        def accept_func(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_result = func(*args, **kwargs)
                if not isinstance(last_result, Response):
                    raise Exception('the {func_name} return value must be a Response'.format(func_name=func.__name__))
                next_params = {}
                for k in restriction:
                    value = last_result.get(k, None)
                    if value is None:
                        raise Exception('the {func_name} missing 1 required positional argument: {key}'.format(
                            func_name=func.__name__, key=k))

                    if not isinstance(value, restriction[k]):
                        raise Exception('{key} must be a {type}'.format(key=k, type=restriction[k].__name__))
                    next_params[k] = value
                if values:
                    next_params.update(values)
                return f(**next_params)
            return wrapper
        return accept_func
    return input_params
