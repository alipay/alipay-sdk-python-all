#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataBillBalancehisQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataBillBalancehisQueryResponse, self).__init__()
        self._beginning_balance = None
        self._ending_balance = None

    @property
    def beginning_balance(self):
        return self._beginning_balance

    @beginning_balance.setter
    def beginning_balance(self, value):
        self._beginning_balance = value
    @property
    def ending_balance(self):
        return self._ending_balance

    @ending_balance.setter
    def ending_balance(self, value):
        self._ending_balance = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataBillBalancehisQueryResponse, self).parse_response_content(response_content)
        if 'beginning_balance' in response:
            self.beginning_balance = response['beginning_balance']
        if 'ending_balance' in response:
            self.ending_balance = response['ending_balance']
