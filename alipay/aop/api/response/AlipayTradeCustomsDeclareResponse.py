#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCustomsDeclareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCustomsDeclareResponse, self).__init__()
        self._alipay_declare_no = None
        self._identity_check = None
        self._trade_no = None

    @property
    def alipay_declare_no(self):
        return self._alipay_declare_no

    @alipay_declare_no.setter
    def alipay_declare_no(self, value):
        self._alipay_declare_no = value
    @property
    def identity_check(self):
        return self._identity_check

    @identity_check.setter
    def identity_check(self, value):
        self._identity_check = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCustomsDeclareResponse, self).parse_response_content(response_content)
        if 'alipay_declare_no' in response:
            self.alipay_declare_no = response['alipay_declare_no']
        if 'identity_check' in response:
            self.identity_check = response['identity_check']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
