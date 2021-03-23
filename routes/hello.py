# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  20:37
@desc:
"""

from config import app


@app.route('/hello')
def hello_world():
    return 'Hello World!'
