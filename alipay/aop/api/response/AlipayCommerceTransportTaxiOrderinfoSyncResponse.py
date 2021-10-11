#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiOrderinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiOrderinfoSyncResponse, self).__init__()
        self._driver_user_id = None
        self._error_code = None
        self._error_msg = None
        self._result = None

    @property
    def driver_user_id(self):
        return self._driver_user_id

    @driver_user_id.setter
    def driver_user_id(self, value):
        self._driver_user_id = value
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
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiOrderinfoSyncResponse, self).parse_response_content(response_content)
        if 'driver_user_id' in response:
            self.driver_user_id = response['driver_user_id']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'result' in response:
            self.result = response['result']
