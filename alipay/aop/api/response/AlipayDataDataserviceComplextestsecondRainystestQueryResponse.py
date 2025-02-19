#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class AlipayDataDataserviceComplextestsecondRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceComplextestsecondRainystestQueryResponse, self).__init__()
        self._response_case = None

    @property
    def response_case(self):
        return self._response_case

    @response_case.setter
    def response_case(self, value):
        if isinstance(value, RainyComplexTypesTheFourth):
            self._response_case = value
        else:
            self._response_case = RainyComplexTypesTheFourth.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceComplextestsecondRainystestQueryResponse, self).parse_response_content(response_content)
        if 'response_case' in response:
            self.response_case = response['response_case']
