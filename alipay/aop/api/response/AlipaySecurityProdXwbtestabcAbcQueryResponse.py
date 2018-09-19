#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdXwbtestabcAbcQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdXwbtestabcAbcQueryResponse, self).__init__()
        self._xwb = None

    @property
    def xwb(self):
        return self._xwb

    @xwb.setter
    def xwb(self, value):
        self._xwb = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdXwbtestabcAbcQueryResponse, self).parse_response_content(response_content)
        if 'xwb' in response:
            self.xwb = response['xwb']
