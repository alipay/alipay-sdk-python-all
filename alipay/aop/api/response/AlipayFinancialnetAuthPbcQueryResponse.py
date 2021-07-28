#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthPbcQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthPbcQueryResponse, self).__init__()
        self._bank_code = None
        self._branch_name = None
        self._city = None
        self._inst_id = None
        self._inst_name = None
        self._provice = None
        self._undertake_inst = None

    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
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
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def provice(self):
        return self._provice

    @provice.setter
    def provice(self, value):
        self._provice = value
    @property
    def undertake_inst(self):
        return self._undertake_inst

    @undertake_inst.setter
    def undertake_inst(self, value):
        self._undertake_inst = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthPbcQueryResponse, self).parse_response_content(response_content)
        if 'bank_code' in response:
            self.bank_code = response['bank_code']
        if 'branch_name' in response:
            self.branch_name = response['branch_name']
        if 'city' in response:
            self.city = response['city']
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'inst_name' in response:
            self.inst_name = response['inst_name']
        if 'provice' in response:
            self.provice = response['provice']
        if 'undertake_inst' in response:
            self.undertake_inst = response['undertake_inst']
