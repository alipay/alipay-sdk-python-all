#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerLiferecordSignResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerLiferecordSignResponse, self).__init__()
        self._process_success = None
        self._sub_code = None
        self._sub_code_number = None
        self._sub_message = None
        self._sub_success = None

    @property
    def process_success(self):
        return self._process_success

    @process_success.setter
    def process_success(self, value):
        self._process_success = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value
    @property
    def sub_code_number(self):
        return self._sub_code_number

    @sub_code_number.setter
    def sub_code_number(self, value):
        self._sub_code_number = value
    @property
    def sub_message(self):
        return self._sub_message

    @sub_message.setter
    def sub_message(self, value):
        self._sub_message = value
    @property
    def sub_success(self):
        return self._sub_success

    @sub_success.setter
    def sub_success(self, value):
        self._sub_success = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerLiferecordSignResponse, self).parse_response_content(response_content)
        if 'process_success' in response:
            self.process_success = response['process_success']
        if 'sub_code' in response:
            self.sub_code = response['sub_code']
        if 'sub_code_number' in response:
            self.sub_code_number = response['sub_code_number']
        if 'sub_message' in response:
            self.sub_message = response['sub_message']
        if 'sub_success' in response:
            self.sub_success = response['sub_success']
