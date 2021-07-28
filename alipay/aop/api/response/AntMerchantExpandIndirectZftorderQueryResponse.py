#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZftSubMerchantOrder import ZftSubMerchantOrder


class AntMerchantExpandIndirectZftorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectZftorderQueryResponse, self).__init__()
        self._orders = None

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, value):
        if isinstance(value, list):
            self._orders = list()
            for i in value:
                if isinstance(i, ZftSubMerchantOrder):
                    self._orders.append(i)
                else:
                    self._orders.append(ZftSubMerchantOrder.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectZftorderQueryResponse, self).parse_response_content(response_content)
        if 'orders' in response:
            self.orders = response['orders']
