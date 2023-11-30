#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneStockMiniappMetaCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockMiniappMetaCreateResponse, self).__init__()
        self._trace = None

    @property
    def trace(self):
        return self._trace

    @trace.setter
    def trace(self, value):
        self._trace = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockMiniappMetaCreateResponse, self).parse_response_content(response_content)
        if 'trace' in response:
            self.trace = response['trace']
