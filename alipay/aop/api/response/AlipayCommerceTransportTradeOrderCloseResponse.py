#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTradeOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTradeOrderCloseResponse, self).__init__()
        self._bill_no = None
        self._out_biz_no = None
        self._out_sub_biz_no = None
        self._trade_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_sub_biz_no(self):
        return self._out_sub_biz_no

    @out_sub_biz_no.setter
    def out_sub_biz_no(self, value):
        self._out_sub_biz_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTradeOrderCloseResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'out_sub_biz_no' in response:
            self.out_sub_biz_no = response['out_sub_biz_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
