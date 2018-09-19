#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskVerifyidentityApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskVerifyidentityApplyResponse, self).__init__()
        self._err_code = None
        self._err_message = None
        self._is_success = None
        self._unusable_product_list = None
        self._usable_product_group = None

    @property
    def err_code(self):
        return self._err_code

    @err_code.setter
    def err_code(self, value):
        self._err_code = value
    @property
    def err_message(self):
        return self._err_message

    @err_message.setter
    def err_message(self, value):
        self._err_message = value
    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def unusable_product_list(self):
        return self._unusable_product_list

    @unusable_product_list.setter
    def unusable_product_list(self, value):
        self._unusable_product_list = value
    @property
    def usable_product_group(self):
        return self._usable_product_group

    @usable_product_group.setter
    def usable_product_group(self, value):
        self._usable_product_group = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskVerifyidentityApplyResponse, self).parse_response_content(response_content)
        if 'err_code' in response:
            self.err_code = response['err_code']
        if 'err_message' in response:
            self.err_message = response['err_message']
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'unusable_product_list' in response:
            self.unusable_product_list = response['unusable_product_list']
        if 'usable_product_group' in response:
            self.usable_product_group = response['usable_product_group']
