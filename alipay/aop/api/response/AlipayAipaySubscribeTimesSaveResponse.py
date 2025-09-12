#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubscribeCountTimeResponse import SubscribeCountTimeResponse


class AlipayAipaySubscribeTimesSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipaySubscribeTimesSaveResponse, self).__init__()
        self._data = None
        self._error_code = None
        self._error_message = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, SubscribeCountTimeResponse):
            self._data = value
        else:
            self._data = SubscribeCountTimeResponse.from_alipay_dict(value)
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipaySubscribeTimesSaveResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
