#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class AlipayDataDataserviceSchematwentysecondRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchematwentysecondRainystestQueryResponse, self).__init__()
        self._demo_case = None
        self._firstlevel_ref = None
        self._firstlevel_string_1 = None
        self._firstlevel_string_2 = None

    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value
    @property
    def firstlevel_ref(self):
        return self._firstlevel_ref

    @firstlevel_ref.setter
    def firstlevel_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourth):
            self._firstlevel_ref = value
        else:
            self._firstlevel_ref = RainyComplexTypesTheFourth.from_alipay_dict(value)
    @property
    def firstlevel_string_1(self):
        return self._firstlevel_string_1

    @firstlevel_string_1.setter
    def firstlevel_string_1(self, value):
        self._firstlevel_string_1 = value
    @property
    def firstlevel_string_2(self):
        return self._firstlevel_string_2

    @firstlevel_string_2.setter
    def firstlevel_string_2(self, value):
        self._firstlevel_string_2 = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchematwentysecondRainystestQueryResponse, self).parse_response_content(response_content)
        if 'demo_case' in response:
            self.demo_case = response['demo_case']
        if 'firstlevel_ref' in response:
            self.firstlevel_ref = response['firstlevel_ref']
        if 'firstlevel_string_1' in response:
            self.firstlevel_string_1 = response['firstlevel_string_1']
        if 'firstlevel_string_2' in response:
            self.firstlevel_string_2 = response['firstlevel_string_2']
