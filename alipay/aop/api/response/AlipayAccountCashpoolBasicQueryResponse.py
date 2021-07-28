#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountCashpoolBasicQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountCashpoolBasicQueryResponse, self).__init__()
        self._count = None
        self._inst_basic_cash_pool_list = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def inst_basic_cash_pool_list(self):
        return self._inst_basic_cash_pool_list

    @inst_basic_cash_pool_list.setter
    def inst_basic_cash_pool_list(self, value):
        if isinstance(value, list):
            self._inst_basic_cash_pool_list = list()
            for i in value:
                self._inst_basic_cash_pool_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayAccountCashpoolBasicQueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'inst_basic_cash_pool_list' in response:
            self.inst_basic_cash_pool_list = response['inst_basic_cash_pool_list']
