#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayDelegationPaytokenApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayDelegationPaytokenApplyResponse, self).__init__()
        self._pay_token = None
        self._valid_end_time = None

    @property
    def pay_token(self):
        return self._pay_token

    @pay_token.setter
    def pay_token(self, value):
        self._pay_token = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayDelegationPaytokenApplyResponse, self).parse_response_content(response_content)
        if 'pay_token' in response:
            self.pay_token = response['pay_token']
        if 'valid_end_time' in response:
            self.valid_end_time = response['valid_end_time']
