#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiDriverlevelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiDriverlevelQueryResponse, self).__init__()
        self._date_version = None
        self._driver_level = None
        self._driver_phone = None
        self._error_code = None
        self._error_message = None
        self._ext_info = None
        self._status = None

    @property
    def date_version(self):
        return self._date_version

    @date_version.setter
    def date_version(self, value):
        self._date_version = value
    @property
    def driver_level(self):
        return self._driver_level

    @driver_level.setter
    def driver_level(self, value):
        self._driver_level = value
    @property
    def driver_phone(self):
        return self._driver_phone

    @driver_phone.setter
    def driver_phone(self, value):
        self._driver_phone = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiDriverlevelQueryResponse, self).parse_response_content(response_content)
        if 'date_version' in response:
            self.date_version = response['date_version']
        if 'driver_level' in response:
            self.driver_level = response['driver_level']
        if 'driver_phone' in response:
            self.driver_phone = response['driver_phone']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'status' in response:
            self.status = response['status']
