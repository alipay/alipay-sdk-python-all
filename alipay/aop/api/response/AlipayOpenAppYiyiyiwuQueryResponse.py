#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppYiyiyiwuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppYiyiyiwuQueryResponse, self).__init__()
        self._chucan = None

    @property
    def chucan(self):
        return self._chucan

    @chucan.setter
    def chucan(self, value):
        self._chucan = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppYiyiyiwuQueryResponse, self).parse_response_content(response_content)
        if 'chucan' in response:
            self.chucan = response['chucan']
