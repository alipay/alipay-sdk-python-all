#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderOpenapi import OrderOpenapi


class AlipayUserUgshoppingOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserUgshoppingOrderQueryResponse, self).__init__()
        self._orders = None

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, value):
        if isinstance(value, list):
            self._orders = list()
            for i in value:
                if isinstance(i, OrderOpenapi):
                    self._orders.append(i)
                else:
                    self._orders.append(OrderOpenapi.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserUgshoppingOrderQueryResponse, self).parse_response_content(response_content)
        if 'orders' in response:
            self.orders = response['orders']
