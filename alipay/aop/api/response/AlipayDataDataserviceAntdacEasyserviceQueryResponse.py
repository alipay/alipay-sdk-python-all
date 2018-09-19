#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAntdacEasyserviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAntdacEasyserviceQueryResponse, self).__init__()
        self._ret_val = None

    @property
    def ret_val(self):
        return self._ret_val

    @ret_val.setter
    def ret_val(self, value):
        self._ret_val = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAntdacEasyserviceQueryResponse, self).parse_response_content(response_content)
        if 'ret_val' in response:
            self.ret_val = response['ret_val']
