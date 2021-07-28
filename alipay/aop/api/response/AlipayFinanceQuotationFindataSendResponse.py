#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinanceQuotationFindataSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceQuotationFindataSendResponse, self).__init__()
        self._send_result = None

    @property
    def send_result(self):
        return self._send_result

    @send_result.setter
    def send_result(self, value):
        self._send_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceQuotationFindataSendResponse, self).parse_response_content(response_content)
        if 'send_result' in response:
            self.send_result = response['send_result']
