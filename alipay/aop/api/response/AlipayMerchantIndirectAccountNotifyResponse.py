#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectAccountNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectAccountNotifyResponse, self).__init__()
        self._result_code = None
        self._result_info = None
        self._result_status = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_info(self):
        return self._result_info

    @result_info.setter
    def result_info(self, value):
        self._result_info = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectAccountNotifyResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_info' in response:
            self.result_info = response['result_info']
        if 'result_status' in response:
            self.result_status = response['result_status']
