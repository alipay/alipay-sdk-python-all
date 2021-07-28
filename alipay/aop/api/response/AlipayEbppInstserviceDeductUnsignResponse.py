#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceDeductUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceDeductUnsignResponse, self).__init__()
        self._error_code = None
        self._process_id = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceDeductUnsignResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'process_id' in response:
            self.process_id = response['process_id']
