#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskGravityWorkflowQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskGravityWorkflowQueryResponse, self).__init__()
        self._code_error = None
        self._code_message = None
        self._last_operate = None
        self._process_success = None
        self._state = None

    @property
    def code_error(self):
        return self._code_error

    @code_error.setter
    def code_error(self, value):
        self._code_error = value
    @property
    def code_message(self):
        return self._code_message

    @code_message.setter
    def code_message(self, value):
        self._code_message = value
    @property
    def last_operate(self):
        return self._last_operate

    @last_operate.setter
    def last_operate(self, value):
        self._last_operate = value
    @property
    def process_success(self):
        return self._process_success

    @process_success.setter
    def process_success(self, value):
        self._process_success = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskGravityWorkflowQueryResponse, self).parse_response_content(response_content)
        if 'code_error' in response:
            self.code_error = response['code_error']
        if 'code_message' in response:
            self.code_message = response['code_message']
        if 'last_operate' in response:
            self.last_operate = response['last_operate']
        if 'process_success' in response:
            self.process_success = response['process_success']
        if 'state' in response:
            self.state = response['state']
