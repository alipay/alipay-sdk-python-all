#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditCreditriskGuarschemeQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditCreditriskGuarschemeQueryResponse, self).__init__()
        self._admit = None
        self._available_amt = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def available_amt(self):
        return self._available_amt

    @available_amt.setter
    def available_amt(self, value):
        self._available_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditCreditriskGuarschemeQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'available_amt' in response:
            self.available_amt = response['available_amt']
