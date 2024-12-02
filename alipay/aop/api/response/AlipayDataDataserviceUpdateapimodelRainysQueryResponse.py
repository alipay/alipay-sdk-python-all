#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceUpdateapimodelRainysQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceUpdateapimodelRainysQueryResponse, self).__init__()
        self._out_array_tc_1 = None

    @property
    def out_array_tc_1(self):
        return self._out_array_tc_1

    @out_array_tc_1.setter
    def out_array_tc_1(self, value):
        if isinstance(value, list):
            self._out_array_tc_1 = list()
            for i in value:
                self._out_array_tc_1.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceUpdateapimodelRainysQueryResponse, self).parse_response_content(response_content)
        if 'out_array_tc_1' in response:
            self.out_array_tc_1 = response['out_array_tc_1']
