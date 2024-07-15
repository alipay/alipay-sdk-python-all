#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheSecond import RainyComplexTypesTheSecond
from alipay.aop.api.domain.RainyComplexTypesTheFirst import RainyComplexTypesTheFirst


class AlipayDataDataexchangeComplextypeRainysQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeComplextypeRainysQueryResponse, self).__init__()
        self._references_test_a = None
        self._references_test_b = None

    @property
    def references_test_a(self):
        return self._references_test_a

    @references_test_a.setter
    def references_test_a(self, value):
        if isinstance(value, RainyComplexTypesTheSecond):
            self._references_test_a = value
        else:
            self._references_test_a = RainyComplexTypesTheSecond.from_alipay_dict(value)
    @property
    def references_test_b(self):
        return self._references_test_b

    @references_test_b.setter
    def references_test_b(self, value):
        if isinstance(value, RainyComplexTypesTheFirst):
            self._references_test_b = value
        else:
            self._references_test_b = RainyComplexTypesTheFirst.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeComplextypeRainysQueryResponse, self).parse_response_content(response_content)
        if 'references_test_a' in response:
            self.references_test_a = response['references_test_a']
        if 'references_test_b' in response:
            self.references_test_b = response['references_test_b']
