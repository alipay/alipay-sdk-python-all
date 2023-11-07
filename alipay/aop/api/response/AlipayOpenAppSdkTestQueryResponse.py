#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppSdkTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppSdkTestQueryResponse, self).__init__()
        self._str_out = None

    @property
    def str_out(self):
        return self._str_out

    @str_out.setter
    def str_out(self, value):
        self._str_out = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppSdkTestQueryResponse, self).parse_response_content(response_content)
        if 'str_out' in response:
            self.str_out = response['str_out']
