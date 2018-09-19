#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppProdmodeUnionbankQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppProdmodeUnionbankQueryResponse, self).__init__()
        self._bank_code = None
        self._bank_name = None
        self._branch_name = None
        self._city = None
        self._prov = None

    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def prov(self):
        return self._prov

    @prov.setter
    def prov(self, value):
        self._prov = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppProdmodeUnionbankQueryResponse, self).parse_response_content(response_content)
        if 'bank_code' in response:
            self.bank_code = response['bank_code']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'branch_name' in response:
            self.branch_name = response['branch_name']
        if 'city' in response:
            self.city = response['city']
        if 'prov' in response:
            self.prov = response['prov']
