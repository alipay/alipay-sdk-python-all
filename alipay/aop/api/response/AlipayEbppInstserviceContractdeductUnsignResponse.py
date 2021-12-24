#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceContractdeductUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceContractdeductUnsignResponse, self).__init__()
        self._process_id = None
        self._result_code = None
        self._result_msg = None
        self._success = None

    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
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
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceContractdeductUnsignResponse, self).parse_response_content(response_content)
        if 'process_id' in response:
            self.process_id = response['process_id']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'success' in response:
            self.success = response['success']
