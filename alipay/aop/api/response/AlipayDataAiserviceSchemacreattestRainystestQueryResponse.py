#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataAiserviceSchemacreattestRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceSchemacreattestRainystestQueryResponse, self).__init__()
        self._demo_case_res = None

    @property
    def demo_case_res(self):
        return self._demo_case_res

    @demo_case_res.setter
    def demo_case_res(self, value):
        self._demo_case_res = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceSchemacreattestRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_case_res' in response:
            self.demo_case_res = response['demo_case_res']
