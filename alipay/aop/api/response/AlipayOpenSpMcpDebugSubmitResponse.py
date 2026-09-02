#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpMcpDebugSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpMcpDebugSubmitResponse, self).__init__()
        self._debug_result_info = None
        self._debug_success = None

    @property
    def debug_result_info(self):
        return self._debug_result_info

    @debug_result_info.setter
    def debug_result_info(self, value):
        self._debug_result_info = value
    @property
    def debug_success(self):
        return self._debug_success

    @debug_success.setter
    def debug_success(self, value):
        self._debug_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpMcpDebugSubmitResponse, self).parse_response_content(response_content)
        if 'debug_result_info' in response:
            self.debug_result_info = response['debug_result_info']
        if 'debug_success' in response:
            self.debug_success = response['debug_success']
