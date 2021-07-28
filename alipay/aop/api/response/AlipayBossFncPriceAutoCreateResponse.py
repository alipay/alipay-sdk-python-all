#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncPriceAutoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncPriceAutoCreateResponse, self).__init__()
        self._result_code = None
        self._result_detail = None
        self._result_msg = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_detail(self):
        return self._result_detail

    @result_detail.setter
    def result_detail(self, value):
        self._result_detail = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncPriceAutoCreateResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_detail' in response:
            self.result_detail = response['result_detail']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
