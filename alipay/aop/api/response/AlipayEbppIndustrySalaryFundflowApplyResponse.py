#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryFundflowApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryFundflowApplyResponse, self).__init__()
        self._account_no = None
        self._end_date = None
        self._merchant_id = None
        self._out_trade_no = None
        self._receipt_no = None
        self._sign_xml = None
        self._start_date = None
        self._type = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
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
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryFundflowApplyResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'receipt_no' in response:
            self.receipt_no = response['receipt_no']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'type' in response:
            self.type = response['type']
