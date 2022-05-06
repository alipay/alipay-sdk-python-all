#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundBailAgreementUpgradeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundBailAgreementUpgradeResponse, self).__init__()
        self._error_code = None
        self._error_msg = None
        self._result_code = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundBailAgreementUpgradeResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'result_code' in response:
            self.result_code = response['result_code']
