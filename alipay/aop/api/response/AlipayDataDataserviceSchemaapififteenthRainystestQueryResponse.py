#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceSchemaapififteenthRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemaapififteenthRainystestQueryResponse, self).__init__()
        self._demo_res = None

    @property
    def demo_res(self):
        return self._demo_res

    @demo_res.setter
    def demo_res(self, value):
        self._demo_res = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemaapififteenthRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_res' in response:
            self.demo_res = response['demo_res']
