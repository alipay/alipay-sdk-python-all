#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvUaIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvUaIdentifyResponse, self).__init__()
        self._host = None
        self._result_code = None
        self._result_map = None
        self._result_msg = None
        self._ret = None
        self._success = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_map(self):
        return self._result_map

    @result_map.setter
    def result_map(self, value):
        self._result_map = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def ret(self):
        return self._ret

    @ret.setter
    def ret(self, value):
        self._ret = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvUaIdentifyResponse, self).parse_response_content(response_content)
        if 'host' in response:
            self.host = response['host']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_map' in response:
            self.result_map = response['result_map']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'ret' in response:
            self.ret = response['ret']
        if 'success' in response:
            self.success = response['success']
