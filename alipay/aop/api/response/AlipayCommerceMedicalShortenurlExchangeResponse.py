#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalShortenurlExchangeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalShortenurlExchangeResponse, self).__init__()
        self._error_message = None
        self._result_code = None
        self._shorten_url = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def shorten_url(self):
        return self._shorten_url

    @shorten_url.setter
    def shorten_url(self, value):
        self._shorten_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalShortenurlExchangeResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'shorten_url' in response:
            self.shorten_url = response['shorten_url']
