#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportWorldDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportWorldDataSyncResponse, self).__init__()
        self._org_error_code = None
        self._org_error_msg = None
        self._response_data = None

    @property
    def org_error_code(self):
        return self._org_error_code

    @org_error_code.setter
    def org_error_code(self, value):
        self._org_error_code = value
    @property
    def org_error_msg(self):
        return self._org_error_msg

    @org_error_msg.setter
    def org_error_msg(self, value):
        self._org_error_msg = value
    @property
    def response_data(self):
        return self._response_data

    @response_data.setter
    def response_data(self, value):
        self._response_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportWorldDataSyncResponse, self).parse_response_content(response_content)
        if 'org_error_code' in response:
            self.org_error_code = response['org_error_code']
        if 'org_error_msg' in response:
            self.org_error_msg = response['org_error_msg']
        if 'response_data' in response:
            self.response_data = response['response_data']
