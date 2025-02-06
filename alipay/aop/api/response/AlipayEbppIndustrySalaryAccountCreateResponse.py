#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryAccountCreateResponse, self).__init__()
        self._bank_card_no = None
        self._bank_cert_name = None
        self._branch_name = None
        self._branch_no = None
        self._merchant_id = None
        self._out_trade_no = None
        self._sign_xml = None

    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_cert_name(self):
        return self._bank_cert_name

    @bank_cert_name.setter
    def bank_cert_name(self, value):
        self._bank_cert_name = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def branch_no(self):
        return self._branch_no

    @branch_no.setter
    def branch_no(self, value):
        self._branch_no = value
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
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryAccountCreateResponse, self).parse_response_content(response_content)
        if 'bank_card_no' in response:
            self.bank_card_no = response['bank_card_no']
        if 'bank_cert_name' in response:
            self.bank_cert_name = response['bank_cert_name']
        if 'branch_name' in response:
            self.branch_name = response['branch_name']
        if 'branch_no' in response:
            self.branch_no = response['branch_no']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
