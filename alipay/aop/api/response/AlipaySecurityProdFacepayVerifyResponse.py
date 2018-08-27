#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFacepayVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFacepayVerifyResponse, self).__init__()
        self._ftoken = None

    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFacepayVerifyResponse, self).parse_response_content(response_content)
        if 'ftoken' in response:
            self.ftoken = response['ftoken']
