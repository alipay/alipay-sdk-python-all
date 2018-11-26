#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdCtidInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdCtidInitializeResponse, self).__init__()
        self._random_data = None
        self._stream_number = None

    @property
    def random_data(self):
        return self._random_data

    @random_data.setter
    def random_data(self, value):
        self._random_data = value
    @property
    def stream_number(self):
        return self._stream_number

    @stream_number.setter
    def stream_number(self, value):
        self._stream_number = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdCtidInitializeResponse, self).parse_response_content(response_content)
        if 'random_data' in response:
            self.random_data = response['random_data']
        if 'stream_number' in response:
            self.stream_number = response['stream_number']
