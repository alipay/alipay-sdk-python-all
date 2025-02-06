#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryElectronicreceiptApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryElectronicreceiptApplyResponse, self).__init__()
        self._merchant_id = None
        self._order_no = None
        self._out_trade_no = None
        self._receipt_no = None
        self._sign_xml = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def receipt_no(self):
        return self._receipt_no

    @receipt_no.setter
    def receipt_no(self, value):
        self._receipt_no = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryElectronicreceiptApplyResponse, self).parse_response_content(response_content)
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'receipt_no' in response:
            self.receipt_no = response['receipt_no']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
