#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEmployeeAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeAddResponse, self).__init__()
        self._employee_id = None
        self._iot_unique_id = None
        self._sign_url = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def iot_unique_id(self):
        return self._iot_unique_id

    @iot_unique_id.setter
    def iot_unique_id(self, value):
        self._iot_unique_id = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeAddResponse, self).parse_response_content(response_content)
        if 'employee_id' in response:
            self.employee_id = response['employee_id']
        if 'iot_unique_id' in response:
            self.iot_unique_id = response['iot_unique_id']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
