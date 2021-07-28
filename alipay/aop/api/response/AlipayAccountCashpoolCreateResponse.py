#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountCashpoolCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountCashpoolCreateResponse, self).__init__()
        self._cash_pool_id = None
        self._cash_pool_name = None

    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
    @property
    def cash_pool_name(self):
        return self._cash_pool_name

    @cash_pool_name.setter
    def cash_pool_name(self, value):
        self._cash_pool_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountCashpoolCreateResponse, self).parse_response_content(response_content)
        if 'cash_pool_id' in response:
            self.cash_pool_id = response['cash_pool_id']
        if 'cash_pool_name' in response:
            self.cash_pool_name = response['cash_pool_name']
