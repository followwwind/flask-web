# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  20:37
@desc: 配置
"""

from flask import Flask
from flask_restplus import Api

from message.logger import init_log

app = Flask(__name__)

# flask api对象
api = Api(
    app,
    version='1.0.0',
    title='API 1.0.0',
    description='API 1.0.0',
    ui=True
)

# 日志对象
log = init_log(None, "server")


# 跨域设置
@app.after_request
def cors(resp):
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Headers', 'Origin, X-Request-With, Content-Type, Accept')
    resp.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, HEAD')