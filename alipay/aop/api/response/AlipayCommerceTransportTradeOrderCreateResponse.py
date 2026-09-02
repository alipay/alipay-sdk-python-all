#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTradeOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTradeOrderCreateResponse, self).__init__()
        self._async_pay_description = None
        self._bill_no = None
        self._is_async_pay = None
        self._out_no = None
        self._trade_no = None

    @property
    def async_pay_description(self):
        return self._async_pay_description

    @async_pay_description.setter
    def async_pay_description(self, value):
        self._async_pay_description = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def is_async_pay(self):
        return self._is_async_pay

    @is_async_pay.setter
    def is_async_pay(self, value):
        self._is_async_pay = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTradeOrderCreateResponse, self).parse_response_content(response_content)
        if 'async_pay_description' in response:
            self.async_pay_description = response['async_pay_description']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'is_async_pay' in response:
            self.is_async_pay = response['is_async_pay']
        if 'out_no' in response:
            self.out_no = response['out_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
