#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeEnterpriseDelegationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeEnterpriseDelegationQueryResponse, self).__init__()
        self._status = None
        self._trade_no = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeEnterpriseDelegationQueryResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
