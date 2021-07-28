#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiDriverSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiDriverSendResponse, self).__init__()
        self._driver_cert_no = None
        self._error_code = None
        self._error_message = None
        self._ext_info = None

    @property
    def driver_cert_no(self):
        return self._driver_cert_no

    @driver_cert_no.setter
    def driver_cert_no(self, value):
        self._driver_cert_no = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiDriverSendResponse, self).parse_response_content(response_content)
        if 'driver_cert_no' in response:
            self.driver_cert_no = response['driver_cert_no']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
