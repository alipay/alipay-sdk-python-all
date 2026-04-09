#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayAgentPaymentVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayAgentPaymentVerifyResponse, self).__init__()
        self._active = None
        self._amount = None
        self._out_trade_no = None
        self._resource_id = None
        self._trade_no = None

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayAgentPaymentVerifyResponse, self).parse_response_content(response_content)
        if 'active' in response:
            self.active = response['active']
        if 'amount' in response:
            self.amount = response['amount']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'resource_id' in response:
            self.resource_id = response['resource_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
