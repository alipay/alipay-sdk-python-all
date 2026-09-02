#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasAccountModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasAccountModifyResponse, self).__init__()
        self._customer_id = None
        self._enterprise_registration_no = None
        self._out_merchant_name = None

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
    def out_merchant_name(self):
        return self._out_merchant_name

    @out_merchant_name.setter
    def out_merchant_name(self, value):
        self._out_merchant_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasAccountModifyResponse, self).parse_response_content(response_content)
        if 'customer_id' in response:
            self.customer_id = response['customer_id']
        if 'enterprise_registration_no' in response:
            self.enterprise_registration_no = response['enterprise_registration_no']
        if 'out_merchant_name' in response:
            self.out_merchant_name = response['out_merchant_name']
