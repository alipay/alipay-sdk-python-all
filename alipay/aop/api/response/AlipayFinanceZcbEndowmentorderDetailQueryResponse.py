#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EndowmentOrder import EndowmentOrder


class AlipayFinanceZcbEndowmentorderDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceZcbEndowmentorderDetailQueryResponse, self).__init__()
        self._order_list = None
        self._total_amount = None
        self._total_count = None

    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, EndowmentOrder):
                    self._order_list.append(i)
                else:
                    self._order_list.append(EndowmentOrder.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceZcbEndowmentorderDetailQueryResponse, self).parse_response_content(response_content)
        if 'order_list' in response:
            self.order_list = response['order_list']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_count' in response:
            self.total_count = response['total_count']
