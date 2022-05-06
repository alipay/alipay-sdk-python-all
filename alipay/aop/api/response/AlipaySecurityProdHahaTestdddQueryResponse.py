#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdHahaTestdddQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdHahaTestdddQueryResponse, self).__init__()
        self._haha = None

    @property
    def haha(self):
        return self._haha

    @haha.setter
    def haha(self, value):
        self._haha = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdHahaTestdddQueryResponse, self).parse_response_content(response_content)
        if 'haha' in response:
            self.haha = response['haha']
