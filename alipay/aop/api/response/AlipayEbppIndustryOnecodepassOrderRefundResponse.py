#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryOnecodepassOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryOnecodepassOrderRefundResponse, self).__init__()
        self._fund_status = None
        self._refund_fee = None
        self._trade_no = None

    @property
    def fund_status(self):
        return self._fund_status

    @fund_status.setter
    def fund_status(self, value):
        self._fund_status = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryOnecodepassOrderRefundResponse, self).parse_response_content(response_content)
        if 'fund_status' in response:
            self.fund_status = response['fund_status']
        if 'refund_fee' in response:
            self.refund_fee = response['refund_fee']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
