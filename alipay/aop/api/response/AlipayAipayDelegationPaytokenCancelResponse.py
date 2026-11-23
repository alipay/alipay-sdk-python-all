#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayDelegationPaytokenCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayDelegationPaytokenCancelResponse, self).__init__()
        self._pay_token = None
        self._status = None

    @property
    def pay_token(self):
        return self._pay_token

    @pay_token.setter
    def pay_token(self, value):
        self._pay_token = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayDelegationPaytokenCancelResponse, self).parse_response_content(response_content)
        if 'pay_token' in response:
            self.pay_token = response['pay_token']
        if 'status' in response:
            self.status = response['status']
