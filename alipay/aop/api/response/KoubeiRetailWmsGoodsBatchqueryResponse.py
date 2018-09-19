#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GoodsVO import GoodsVO


class KoubeiRetailWmsGoodsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsGoodsBatchqueryResponse, self).__init__()
        self._goods = None
        self._total_count = None

    @property
    def goods(self):
        return self._goods

    @goods.setter
    def goods(self, value):
        if isinstance(value, list):
            self._goods = list()
            for i in value:
                if isinstance(i, GoodsVO):
                    self._goods.append(i)
                else:
                    self._goods.append(GoodsVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsGoodsBatchqueryResponse, self).parse_response_content(response_content)
        if 'goods' in response:
            self.goods = response['goods']
        if 'total_count' in response:
            self.total_count = response['total_count']
