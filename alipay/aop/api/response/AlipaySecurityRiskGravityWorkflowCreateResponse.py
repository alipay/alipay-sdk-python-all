#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskGravityWorkflowCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskGravityWorkflowCreateResponse, self).__init__()
        self._code_error = None
        self._error_message = None
        self._process_success = None
        self._pu_id = None

    @property
    def code_error(self):
        return self._code_error

    @code_error.setter
    def code_error(self, value):
        self._code_error = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def process_success(self):
        return self._process_success

    @process_success.setter
    def process_success(self, value):
        self._process_success = value
    @property
    def pu_id(self):
        return self._pu_id

    @pu_id.setter
    def pu_id(self, value):
        self._pu_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskGravityWorkflowCreateResponse, self).parse_response_content(response_content)
        if 'code_error' in response:
            self.code_error = response['code_error']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'process_success' in response:
            self.process_success = response['process_success']
        if 'pu_id' in response:
            self.pu_id = response['pu_id']
