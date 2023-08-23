#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJfSignConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfSignConsultResponse, self).__init__()
        self._result_code = None
        self._result_msg = None
        self._sign_allowed = None

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
    def sign_allowed(self):
        return self._sign_allowed

    @sign_allowed.setter
    def sign_allowed(self, value):
        self._sign_allowed = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfSignConsultResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'sign_allowed' in response:
            self.sign_allowed = response['sign_allowed']
