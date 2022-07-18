#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityDanielTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDanielTestQueryResponse, self).__init__()
        self._out_param = None

    @property
    def out_param(self):
        return self._out_param

    @out_param.setter
    def out_param(self, value):
        self._out_param = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDanielTestQueryResponse, self).parse_response_content(response_content)
        if 'out_param' in response:
            self.out_param = response['out_param']
