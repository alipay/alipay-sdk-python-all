#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityAppinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityAppinfoQueryResponse, self).__init__()
        self._bbb = None

    @property
    def bbb(self):
        return self._bbb

    @bbb.setter
    def bbb(self, value):
        self._bbb = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityAppinfoQueryResponse, self).parse_response_content(response_content)
        if 'bbb' in response:
            self.bbb = response['bbb']
