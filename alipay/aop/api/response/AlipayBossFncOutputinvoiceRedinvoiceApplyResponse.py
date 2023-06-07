#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncOutputinvoiceRedinvoiceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncOutputinvoiceRedinvoiceApplyResponse, self).__init__()
        self._result_code = None
        self._result_desp = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desp(self):
        return self._result_desp

    @result_desp.setter
    def result_desp(self, value):
        self._result_desp = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncOutputinvoiceRedinvoiceApplyResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desp' in response:
            self.result_desp = response['result_desp']
