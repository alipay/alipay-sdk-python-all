#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppSmartwearManagementSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppSmartwearManagementSyncResponse, self).__init__()
        self._payload = None
        self._result_code = None
        self._result_msg = None

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppSmartwearManagementSyncResponse, self).parse_response_content(response_content)
        if 'payload' in response:
            self.payload = response['payload']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
