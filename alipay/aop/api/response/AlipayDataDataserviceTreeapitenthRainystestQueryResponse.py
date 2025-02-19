#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceTreeapitenthRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceTreeapitenthRainystestQueryResponse, self).__init__()
        self._demo_case = None

    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceTreeapitenthRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_case' in response:
            self.demo_case = response['demo_case']
