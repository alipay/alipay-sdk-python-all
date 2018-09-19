#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPassTplUpdateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPassTplUpdateResponse, self).__init__()
        self._error_code = None
        self._result = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayPassTplUpdateResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'result' in response:
            self.result = response['result']
        if 'success' in response:
            self.success = response['success']
