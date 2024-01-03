#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletPayurlApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletPayurlApplyResponse, self).__init__()
        self._payment_url = None

    @property
    def payment_url(self):
        return self._payment_url

    @payment_url.setter
    def payment_url(self, value):
        self._payment_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletPayurlApplyResponse, self).parse_response_content(response_content)
        if 'payment_url' in response:
            self.payment_url = response['payment_url']
