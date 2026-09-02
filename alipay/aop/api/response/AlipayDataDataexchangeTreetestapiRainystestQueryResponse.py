#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataexchangeTreetestapiRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeTreetestapiRainystestQueryResponse, self).__init__()
        self._demo = None
        self._demo_0525_out = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_0525_out(self):
        return self._demo_0525_out

    @demo_0525_out.setter
    def demo_0525_out(self, value):
        self._demo_0525_out = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeTreetestapiRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo' in response:
            self.demo = response['demo']
        if 'demo_0525_out' in response:
            self.demo_0525_out = response['demo_0525_out']
