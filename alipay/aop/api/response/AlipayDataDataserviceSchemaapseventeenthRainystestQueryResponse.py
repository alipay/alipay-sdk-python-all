#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainysComplexRefFirst import RainysComplexRefFirst
from alipay.aop.api.domain.RainysComplexRefSecond import RainysComplexRefSecond


class AlipayDataDataserviceSchemaapseventeenthRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemaapseventeenthRainystestQueryResponse, self).__init__()
        self._demo_ref = None
        self._demo_weak_ref = None

    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainysComplexRefFirst):
            self._demo_ref = value
        else:
            self._demo_ref = RainysComplexRefFirst.from_alipay_dict(value)
    @property
    def demo_weak_ref(self):
        return self._demo_weak_ref

    @demo_weak_ref.setter
    def demo_weak_ref(self, value):
        if isinstance(value, RainysComplexRefSecond):
            self._demo_weak_ref = value
        else:
            self._demo_weak_ref = RainysComplexRefSecond.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemaapseventeenthRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_ref' in response:
            self.demo_ref = response['demo_ref']
        if 'demo_weak_ref' in response:
            self.demo_weak_ref = response['demo_weak_ref']
