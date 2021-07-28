#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMemberTakegcwtaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMemberTakegcwtaskCreateResponse, self).__init__()
        self._flow_id = None
        self._result_code = None
        self._success = None

    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserMemberTakegcwtaskCreateResponse, self).parse_response_content(response_content)
        if 'flow_id' in response:
            self.flow_id = response['flow_id']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'success' in response:
            self.success = response['success']
