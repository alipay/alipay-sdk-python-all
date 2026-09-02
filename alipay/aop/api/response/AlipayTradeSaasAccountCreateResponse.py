#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasAccountCreateResponse, self).__init__()
        self._customer_id = None
        self._enterprise_registration_no = None
        self._inst_account_name = None
        self._inst_account_no = None
        self._inst_name = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def enterprise_registration_no(self):
        return self._enterprise_registration_no

    @enterprise_registration_no.setter
    def enterprise_registration_no(self, value):
        self._enterprise_registration_no = value
    @property
    def inst_account_name(self):
        return self._inst_account_name

    @inst_account_name.setter
    def inst_account_name(self, value):
        self._inst_account_name = value
    @property
    def inst_account_no(self):
        return self._inst_account_no

    @inst_account_no.setter
    def inst_account_no(self, value):
        self._inst_account_no = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasAccountCreateResponse, self).parse_response_content(response_content)
        if 'customer_id' in response:
            self.customer_id = response['customer_id']
        if 'enterprise_registration_no' in response:
            self.enterprise_registration_no = response['enterprise_registration_no']
        if 'inst_account_name' in response:
            self.inst_account_name = response['inst_account_name']
        if 'inst_account_no' in response:
            self.inst_account_no = response['inst_account_no']
        if 'inst_name' in response:
            self.inst_name = response['inst_name']
