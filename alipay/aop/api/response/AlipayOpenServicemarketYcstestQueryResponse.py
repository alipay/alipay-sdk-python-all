#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenServicemarketYcstestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenServicemarketYcstestQueryResponse, self).__init__()
        self._out_1 = None
        self._out_2 = None

    @property
    def out_1(self):
        return self._out_1

    @out_1.setter
    def out_1(self, value):
        self._out_1 = value
    @property
    def out_2(self):
        return self._out_2

    @out_2.setter
    def out_2(self, value):
        self._out_2 = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenServicemarketYcstestQueryResponse, self).parse_response_content(response_content)
        if 'out_1' in response:
            self.out_1 = response['out_1']
        if 'out_2' in response:
            self.out_2 = response['out_2']
