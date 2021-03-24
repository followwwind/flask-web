# -*- encoding:utf-8 -*-
"""
@author：wind
@time：2021/3/24  19:25
@desc:
"""

from config import db
from message.decorator import Response


class AssertInfoModel(object):

    @staticmethod
    def insert(assert_info):
        _id = db.insert_one('assert', assert_info)
        return Response(_id=_id)

    @staticmethod
    def update(assert_info):
        doc = db.update('assert', assert_info)
        if not doc:
            return Response({})
        return Response(_id=doc['_id'])

    @staticmethod
    def get(assert_info):
        doc = db.query_one('assert', assert_info)
        if not doc:
            return Response({})
        return Response(_id=doc['_id'], dateTime=doc['date_time'], balanceEth=doc['balance_eth']
                        , balanceBusd=doc['balance_busd'], curPriceETH=doc['cur_price_ETH'],  realValueAll=doc['real_value_all'],
                        profit=doc['profit'], profitPct=doc['profit_pct'])

    @staticmethod
    def delete(assert_info):
        doc = db.remove('assert', assert_info)
        if not doc:
            return Response({})
        return Response(_id=doc['_id'])

    @staticmethod
    def list(assert_info, page_num, page_size):
        total_count = db.query_count('assert', assert_info)
        data_list = db.query_search_page('assert', assert_info, page_num, page_size)
        return Response(total=total_count, data=data_list, pageNum=page_num, pageSize=page_size)
