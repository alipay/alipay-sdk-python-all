#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeFinancePrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeFinancePrecreateResponse, self).__init__()
        self._result_code = None
        self._settlement_no = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def settlement_no(self):
        return self._settlement_no

    @settlement_no.setter
    def settlement_no(self, value):
        self._settlement_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeFinancePrecreateResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'settlement_no' in response:
            self.settlement_no = response['settlement_no']
