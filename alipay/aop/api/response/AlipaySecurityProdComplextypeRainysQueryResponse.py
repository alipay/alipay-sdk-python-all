#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheSecond import RainyComplexTypesTheSecond


class AlipaySecurityProdComplextypeRainysQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdComplextypeRainysQueryResponse, self).__init__()
        self._references_test_a = None

    @property
    def references_test_a(self):
        return self._references_test_a

    @references_test_a.setter
    def references_test_a(self, value):
        if isinstance(value, RainyComplexTypesTheSecond):
            self._references_test_a = value
        else:
            self._references_test_a = RainyComplexTypesTheSecond.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdComplextypeRainysQueryResponse, self).parse_response_content(response_content)
        if 'references_test_a' in response:
            self.references_test_a = response['references_test_a']
