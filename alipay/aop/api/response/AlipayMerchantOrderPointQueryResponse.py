#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantOrderPointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantOrderPointQueryResponse, self).__init__()
        self._balance = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantOrderPointQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
