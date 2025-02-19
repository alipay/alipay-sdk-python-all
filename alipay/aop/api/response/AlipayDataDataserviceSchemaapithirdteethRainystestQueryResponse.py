#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceSchemaapithirdteethRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemaapithirdteethRainystestQueryResponse, self).__init__()
        self._demo_response = None

    @property
    def demo_response(self):
        return self._demo_response

    @demo_response.setter
    def demo_response(self, value):
        self._demo_response = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemaapithirdteethRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_response' in response:
            self.demo_response = response['demo_response']
