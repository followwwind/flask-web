# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/23  20:41
@desc:
"""

# 初始化日志
import logging
from logging import handlers


def init_log(conf, name):
    level_name = "INFO"
    deploy = "dev"
    if conf is not None and type(conf) is dict:
        level_name = conf['log']['level']
        deploy = conf['env']['deploy']
    logger = logging.getLogger(name)
    level = logging.getLevelName(level_name)
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s [%(pathname)s:%(funcName)s:%(lineno)d] %(message)s')
    file_handler = handlers.RotatingFileHandler('logs/server.log', maxBytes=2 ** 30, encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)
    if deploy == "dev":
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.DEBUG)
        logger.addHandler(stream_handler)
    return logger
