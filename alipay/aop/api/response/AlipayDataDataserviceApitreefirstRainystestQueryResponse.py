#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheFifteen import RainyComplexTypesTheFifteen


class AlipayDataDataserviceApitreefirstRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceApitreefirstRainystestQueryResponse, self).__init__()
        self._demo_response = None

    @property
    def demo_response(self):
        return self._demo_response

    @demo_response.setter
    def demo_response(self, value):
        if isinstance(value, RainyComplexTypesTheFifteen):
            self._demo_response = value
        else:
            self._demo_response = RainyComplexTypesTheFifteen.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceApitreefirstRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_response' in response:
            self.demo_response = response['demo_response']
