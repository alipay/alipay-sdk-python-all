#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryPerformOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryPerformOrderRefundResponse, self).__init__()
        self._bill_amount = None
        self._bill_no = None
        self._inst_code = None
        self._out_no = None
        self._pay_amount = None
        self._refund_amount = None
        self._service_code = None
        self._trade_no = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryPerformOrderRefundResponse, self).parse_response_content(response_content)
        if 'bill_amount' in response:
            self.bill_amount = response['bill_amount']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'inst_code' in response:
            self.inst_code = response['inst_code']
        if 'out_no' in response:
            self.out_no = response['out_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'service_code' in response:
            self.service_code = response['service_code']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
