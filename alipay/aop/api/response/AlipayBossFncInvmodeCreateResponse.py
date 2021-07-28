#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncInvmodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncInvmodeCreateResponse, self).__init__()
        self._is_success = None
        self._result_code = None

    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncInvmodeCreateResponse, self).parse_response_content(response_content)
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'result_code' in response:
            self.result_code = response['result_code']
