#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntProdpaasTttDetectResponse(AlipayResponse):

    def __init__(self):
        super(AntProdpaasTttDetectResponse, self).__init__()
        self._mobile = None
        self._oo = None

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def oo(self):
        return self._oo

    @oo.setter
    def oo(self, value):
        self._oo = value

    def parse_response_content(self, response_content):
        response = super(AntProdpaasTttDetectResponse, self).parse_response_content(response_content)
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'oo' in response:
            self.oo = response['oo']
