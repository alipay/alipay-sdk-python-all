#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheThirteen import RainyComplexTypesTheThirteen


class AlipayDataDataserviceSchemthirtyfifthRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemthirtyfifthRainystestQueryResponse, self).__init__()
        self._demo_ref = None
        self._demo_str_1 = None
        self._demo_str_2 = None

    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainyComplexTypesTheThirteen):
            self._demo_ref = value
        else:
            self._demo_ref = RainyComplexTypesTheThirteen.from_alipay_dict(value)
    @property
    def demo_str_1(self):
        return self._demo_str_1

    @demo_str_1.setter
    def demo_str_1(self, value):
        self._demo_str_1 = value
    @property
    def demo_str_2(self):
        return self._demo_str_2

    @demo_str_2.setter
    def demo_str_2(self, value):
        self._demo_str_2 = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemthirtyfifthRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_ref' in response:
            self.demo_ref = response['demo_ref']
        if 'demo_str_1' in response:
            self.demo_str_1 = response['demo_str_1']
        if 'demo_str_2' in response:
            self.demo_str_2 = response['demo_str_2']
