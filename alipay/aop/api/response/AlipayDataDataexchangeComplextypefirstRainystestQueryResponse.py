#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst
from alipay.aop.api.domain.RainyComplexTypesTheFirst import RainyComplexTypesTheFirst


class AlipayDataDataexchangeComplextypefirstRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeComplextypefirstRainystestQueryResponse, self).__init__()
        self._schema_response_01 = None
        self._schema_response_02 = None

    @property
    def schema_response_01(self):
        return self._schema_response_01

    @schema_response_01.setter
    def schema_response_01(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFirst):
            self._schema_response_01 = value
        else:
            self._schema_response_01 = RainyComplexTypesRefWeakFirst.from_alipay_dict(value)
    @property
    def schema_response_02(self):
        return self._schema_response_02

    @schema_response_02.setter
    def schema_response_02(self, value):
        if isinstance(value, RainyComplexTypesTheFirst):
            self._schema_response_02 = value
        else:
            self._schema_response_02 = RainyComplexTypesTheFirst.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeComplextypefirstRainystestQueryResponse, self).parse_response_content(response_content)
        if 'schema_response_01' in response:
            self.schema_response_01 = response['schema_response_01']
        if 'schema_response_02' in response:
            self.schema_response_02 = response['schema_response_02']
