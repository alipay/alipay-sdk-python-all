#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenDanielTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenDanielTestQueryResponse, self).__init__()
        self._out_put = None

    @property
    def out_put(self):
        return self._out_put

    @out_put.setter
    def out_put(self, value):
        self._out_put = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenDanielTestQueryResponse, self).parse_response_content(response_content)
        if 'out_put' in response:
            self.out_put = response['out_put']
