#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationPointBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationPointBalanceQueryResponse, self).__init__()
        self._balance = None
        self._to_expired_point = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def to_expired_point(self):
        return self._to_expired_point

    @to_expired_point.setter
    def to_expired_point(self, value):
        self._to_expired_point = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationPointBalanceQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'to_expired_point' in response:
            self.to_expired_point = response['to_expired_point']
