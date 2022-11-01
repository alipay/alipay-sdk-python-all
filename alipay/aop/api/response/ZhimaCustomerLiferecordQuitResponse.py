#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerLiferecordQuitResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerLiferecordQuitResponse, self).__init__()
        self._operate_success = None
        self._res_code = None
        self._sub_code_number = None
        self._sub_message = None
        self._sub_success = None

    @property
    def operate_success(self):
        return self._operate_success

    @operate_success.setter
    def operate_success(self, value):
        self._operate_success = value
    @property
    def res_code(self):
        return self._res_code

    @res_code.setter
    def res_code(self, value):
        self._res_code = value
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
        response = super(ZhimaCustomerLiferecordQuitResponse, self).parse_response_content(response_content)
        if 'operate_success' in response:
            self.operate_success = response['operate_success']
        if 'res_code' in response:
            self.res_code = response['res_code']
        if 'sub_code_number' in response:
            self.sub_code_number = response['sub_code_number']
        if 'sub_message' in response:
            self.sub_message = response['sub_message']
        if 'sub_success' in response:
            self.sub_success = response['sub_success']
