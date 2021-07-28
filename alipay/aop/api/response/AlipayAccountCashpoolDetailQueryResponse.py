#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountCashpoolDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountCashpoolDetailQueryResponse, self).__init__()
        self._cash_pool_detail = None

    @property
    def cash_pool_detail(self):
        return self._cash_pool_detail

    @cash_pool_detail.setter
    def cash_pool_detail(self, value):
        self._cash_pool_detail = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountCashpoolDetailQueryResponse, self).parse_response_content(response_content)
        if 'cash_pool_detail' in response:
            self.cash_pool_detail = response['cash_pool_detail']
