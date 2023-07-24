#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAccountInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountInfoQueryResponse, self).__init__()
        self._enable_payment = None

    @property
    def enable_payment(self):
        return self._enable_payment

    @enable_payment.setter
    def enable_payment(self, value):
        self._enable_payment = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountInfoQueryResponse, self).parse_response_content(response_content)
        if 'enable_payment' in response:
            self.enable_payment = response['enable_payment']
