#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryPayrollaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryPayrollaccountQueryResponse, self).__init__()
        self._acct_map = None
        self._acct_type = None
        self._merchant_id = None
        self._merchant_name = None
        self._sign_xml = None

    @property
    def acct_map(self):
        return self._acct_map

    @acct_map.setter
    def acct_map(self, value):
        self._acct_map = value
    @property
    def acct_type(self):
        return self._acct_type

    @acct_type.setter
    def acct_type(self, value):
        self._acct_type = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryPayrollaccountQueryResponse, self).parse_response_content(response_content)
        if 'acct_map' in response:
            self.acct_map = response['acct_map']
        if 'acct_type' in response:
            self.acct_type = response['acct_type']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
