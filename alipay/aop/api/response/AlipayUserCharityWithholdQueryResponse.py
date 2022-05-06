#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCharityWithholdQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCharityWithholdQueryResponse, self).__init__()
        self._result_code = None
        self._trade_no = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCharityWithholdQueryResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
