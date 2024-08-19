#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceCodecheckRainyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceCodecheckRainyQueryResponse, self).__init__()
        self._aaa = None

    @property
    def aaa(self):
        return self._aaa

    @aaa.setter
    def aaa(self, value):
        self._aaa = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceCodecheckRainyQueryResponse, self).parse_response_content(response_content)
        if 'aaa' in response:
            self.aaa = response['aaa']
