#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIndirectmerchantCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIndirectmerchantCreateResponse, self).__init__()
        self._merchant_pid = None

    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIndirectmerchantCreateResponse, self).parse_response_content(response_content)
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
