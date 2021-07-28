#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeDepositVerifyApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeDepositVerifyApplyResponse, self).__init__()
        self._request_no = None
        self._verify_id = None

    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeDepositVerifyApplyResponse, self).parse_response_content(response_content)
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
