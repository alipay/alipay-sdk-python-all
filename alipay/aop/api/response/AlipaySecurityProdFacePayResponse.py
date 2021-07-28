#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFacePayResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFacePayResponse, self).__init__()
        self._aa = None

    @property
    def aa(self):
        return self._aa

    @aa.setter
    def aa(self, value):
        self._aa = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFacePayResponse, self).parse_response_content(response_content)
        if 'aa' in response:
            self.aa = response['aa']
