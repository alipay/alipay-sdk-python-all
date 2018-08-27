#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppXwbtestabcQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppXwbtestabcQueryResponse, self).__init__()
        self._xw = None

    @property
    def xw(self):
        return self._xw

    @xw.setter
    def xw(self, value):
        self._xw = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppXwbtestabcQueryResponse, self).parse_response_content(response_content)
        if 'xw' in response:
            self.xw = response['xw']
