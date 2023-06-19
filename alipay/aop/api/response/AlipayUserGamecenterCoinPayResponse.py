#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGamecenterCoinPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGamecenterCoinPayResponse, self).__init__()
        self._balance = None
        self._deduct_no = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def deduct_no(self):
        return self._deduct_no

    @deduct_no.setter
    def deduct_no(self, value):
        self._deduct_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGamecenterCoinPayResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'deduct_no' in response:
            self.deduct_no = response['deduct_no']
