#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainysComplexRefSixth import RainysComplexRefSixth
from alipay.aop.api.domain.RainyComplexTypesTheNinth import RainyComplexTypesTheNinth
from alipay.aop.api.domain.RainysComplexRefSeventh import RainysComplexRefSeventh


class AlipayDataDataserviceSchemaapininteenthRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemaapininteenthRainystestQueryResponse, self).__init__()
        self._demo_object_1 = None
        self._demo_strong = None
        self._demo_weak = None

    @property
    def demo_object_1(self):
        return self._demo_object_1

    @demo_object_1.setter
    def demo_object_1(self, value):
        if isinstance(value, RainysComplexRefSixth):
            self._demo_object_1 = value
        else:
            self._demo_object_1 = RainysComplexRefSixth.from_alipay_dict(value)
    @property
    def demo_strong(self):
        return self._demo_strong

    @demo_strong.setter
    def demo_strong(self, value):
        if isinstance(value, RainyComplexTypesTheNinth):
            self._demo_strong = value
        else:
            self._demo_strong = RainyComplexTypesTheNinth.from_alipay_dict(value)
    @property
    def demo_weak(self):
        return self._demo_weak

    @demo_weak.setter
    def demo_weak(self, value):
        if isinstance(value, RainysComplexRefSeventh):
            self._demo_weak = value
        else:
            self._demo_weak = RainysComplexRefSeventh.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemaapininteenthRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_object_1' in response:
            self.demo_object_1 = response['demo_object_1']
        if 'demo_strong' in response:
            self.demo_strong = response['demo_strong']
        if 'demo_weak' in response:
            self.demo_weak = response['demo_weak']
