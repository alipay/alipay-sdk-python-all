#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeFinanceAdvanceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeFinanceAdvanceApplyResponse, self).__init__()
        self._ext_info = None
        self._result_code = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeFinanceAdvanceApplyResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'result_code' in response:
            self.result_code = response['result_code']
