#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFacePayCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFacePayCreateResponse, self).__init__()
        self._bbb = None

    @property
    def bbb(self):
        return self._bbb

    @bbb.setter
    def bbb(self, value):
        self._bbb = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFacePayCreateResponse, self).parse_response_content(response_content)
        if 'bbb' in response:
            self.bbb = response['bbb']
