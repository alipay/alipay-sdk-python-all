#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyPraviteTestForUploadComplexInfo import RainyPraviteTestForUploadComplexInfo


class AlipayDataDataexchangeTreeapiuploadtestRainytestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeTreeapiuploadtestRainytestQueryResponse, self).__init__()
        self._demo = None
        self._ref = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def ref(self):
        return self._ref

    @ref.setter
    def ref(self, value):
        if isinstance(value, RainyPraviteTestForUploadComplexInfo):
            self._ref = value
        else:
            self._ref = RainyPraviteTestForUploadComplexInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeTreeapiuploadtestRainytestQueryResponse, self).parse_response_content(response_content)
        if 'demo' in response:
            self.demo = response['demo']
        if 'ref' in response:
            self.ref = response['ref']
