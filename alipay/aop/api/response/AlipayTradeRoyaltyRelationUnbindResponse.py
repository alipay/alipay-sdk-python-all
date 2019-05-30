#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeRoyaltyRelationUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRoyaltyRelationUnbindResponse, self).__init__()
        self._result_code = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRoyaltyRelationUnbindResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
