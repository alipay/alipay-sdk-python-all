#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdMyGetchyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdMyGetchyQueryResponse, self).__init__()
        self._chen = None

    @property
    def chen(self):
        return self._chen

    @chen.setter
    def chen(self, value):
        self._chen = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdMyGetchyQueryResponse, self).parse_response_content(response_content)
        if 'chen' in response:
            self.chen = response['chen']
