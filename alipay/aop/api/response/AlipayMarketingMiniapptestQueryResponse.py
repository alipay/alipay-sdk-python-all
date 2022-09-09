#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingMiniapptestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingMiniapptestQueryResponse, self).__init__()
        self._sadsad = None

    @property
    def sadsad(self):
        return self._sadsad

    @sadsad.setter
    def sadsad(self, value):
        self._sadsad = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingMiniapptestQueryResponse, self).parse_response_content(response_content)
        if 'sadsad' in response:
            self.sadsad = response['sadsad']
