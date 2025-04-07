#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainysComplexRefForth import RainysComplexRefForth
from alipay.aop.api.domain.RainysComplexRefFifth import RainysComplexRefFifth


class AlipayDataDataserviceSchemaapieighteenthRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemaapieighteenthRainystestQueryResponse, self).__init__()
        self._demo_object_1 = None
        self._demo_weak = None

    @property
    def demo_object_1(self):
        return self._demo_object_1

    @demo_object_1.setter
    def demo_object_1(self, value):
        if isinstance(value, RainysComplexRefForth):
            self._demo_object_1 = value
        else:
            self._demo_object_1 = RainysComplexRefForth.from_alipay_dict(value)
    @property
    def demo_weak(self):
        return self._demo_weak

    @demo_weak.setter
    def demo_weak(self, value):
        if isinstance(value, RainysComplexRefFifth):
            self._demo_weak = value
        else:
            self._demo_weak = RainysComplexRefFifth.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemaapieighteenthRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_object_1' in response:
            self.demo_object_1 = response['demo_object_1']
        if 'demo_weak' in response:
            self.demo_weak = response['demo_weak']
