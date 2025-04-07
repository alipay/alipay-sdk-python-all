#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainysComplexRefThird import RainysComplexRefThird
from alipay.aop.api.domain.RainyComplexTypesTheEighth import RainyComplexTypesTheEighth


class AlipayDataDataserviceSchemaapisixteenthRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemaapisixteenthRainystestQueryResponse, self).__init__()
        self._demo_object = None
        self._demo_weak = None

    @property
    def demo_object(self):
        return self._demo_object

    @demo_object.setter
    def demo_object(self, value):
        if isinstance(value, RainysComplexRefThird):
            self._demo_object = value
        else:
            self._demo_object = RainysComplexRefThird.from_alipay_dict(value)
    @property
    def demo_weak(self):
        return self._demo_weak

    @demo_weak.setter
    def demo_weak(self, value):
        if isinstance(value, RainyComplexTypesTheEighth):
            self._demo_weak = value
        else:
            self._demo_weak = RainyComplexTypesTheEighth.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemaapisixteenthRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_object' in response:
            self.demo_object = response['demo_object']
        if 'demo_weak' in response:
            self.demo_weak = response['demo_weak']
