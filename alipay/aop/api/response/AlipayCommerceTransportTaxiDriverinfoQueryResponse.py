#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiDriverinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiDriverinfoQueryResponse, self).__init__()
        self._driver_age = None
        self._driver_name = None
        self._error_code = None
        self._error_msg = None
        self._sys_driver_id = None

    @property
    def driver_age(self):
        return self._driver_age

    @driver_age.setter
    def driver_age(self, value):
        self._driver_age = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def sys_driver_id(self):
        return self._sys_driver_id

    @sys_driver_id.setter
    def sys_driver_id(self, value):
        self._sys_driver_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiDriverinfoQueryResponse, self).parse_response_content(response_content)
        if 'driver_age' in response:
            self.driver_age = response['driver_age']
        if 'driver_name' in response:
            self.driver_name = response['driver_name']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'sys_driver_id' in response:
            self.sys_driver_id = response['sys_driver_id']
