#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheSecond import RainyComplexTypesTheSecond
from alipay.aop.api.domain.RainyComplexTypeRefWeakFirst import RainyComplexTypeRefWeakFirst


class AlipayDataDataserviceSchemacomplextwiceRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemacomplextwiceRainystestQueryResponse, self).__init__()
        self._demo_strong_complextype = None
        self._demo_weak_complextype = None

    @property
    def demo_strong_complextype(self):
        return self._demo_strong_complextype

    @demo_strong_complextype.setter
    def demo_strong_complextype(self, value):
        if isinstance(value, RainyComplexTypesTheSecond):
            self._demo_strong_complextype = value
        else:
            self._demo_strong_complextype = RainyComplexTypesTheSecond.from_alipay_dict(value)
    @property
    def demo_weak_complextype(self):
        return self._demo_weak_complextype

    @demo_weak_complextype.setter
    def demo_weak_complextype(self, value):
        if isinstance(value, RainyComplexTypeRefWeakFirst):
            self._demo_weak_complextype = value
        else:
            self._demo_weak_complextype = RainyComplexTypeRefWeakFirst.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemacomplextwiceRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_strong_complextype' in response:
            self.demo_strong_complextype = response['demo_strong_complextype']
        if 'demo_weak_complextype' in response:
            self.demo_weak_complextype = response['demo_weak_complextype']
