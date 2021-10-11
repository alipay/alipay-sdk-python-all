#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiDriverstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiDriverstatusQueryResponse, self).__init__()
        self._app_time_stamp = None
        self._error_code = None
        self._error_msg = None
        self._server_time_stamp = None
        self._status = None
        self._sub_status = None

    @property
    def app_time_stamp(self):
        return self._app_time_stamp

    @app_time_stamp.setter
    def app_time_stamp(self, value):
        self._app_time_stamp = value
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
    def server_time_stamp(self):
        return self._server_time_stamp

    @server_time_stamp.setter
    def server_time_stamp(self, value):
        self._server_time_stamp = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiDriverstatusQueryResponse, self).parse_response_content(response_content)
        if 'app_time_stamp' in response:
            self.app_time_stamp = response['app_time_stamp']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'server_time_stamp' in response:
            self.server_time_stamp = response['server_time_stamp']
        if 'status' in response:
            self.status = response['status']
        if 'sub_status' in response:
            self.sub_status = response['sub_status']
