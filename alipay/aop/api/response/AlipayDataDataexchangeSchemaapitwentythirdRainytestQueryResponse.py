#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyComplexTypesRefWeakFifth import RainyComplexTypesRefWeakFifth
from alipay.aop.api.domain.RainyComplexTypesTheThirteen import RainyComplexTypesTheThirteen
from alipay.aop.api.domain.RainyComplexTypesTheFourteenOne import RainyComplexTypesTheFourteenOne
from alipay.aop.api.domain.RainyComplexTypesTheThirteen import RainyComplexTypesTheThirteen


class AlipayDataDataexchangeSchemaapitwentythirdRainytestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeSchemaapitwentythirdRainytestQueryResponse, self).__init__()
        self._demo_ref = None
        self._demo_res = None
        self._demo_strong_ref = None
        self._demo_wink_ref = None
        self._test = None

    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFifth):
            self._demo_ref = value
        else:
            self._demo_ref = RainyComplexTypesRefWeakFifth.from_alipay_dict(value)
    @property
    def demo_res(self):
        return self._demo_res

    @demo_res.setter
    def demo_res(self, value):
        self._demo_res = value
    @property
    def demo_strong_ref(self):
        return self._demo_strong_ref

    @demo_strong_ref.setter
    def demo_strong_ref(self, value):
        if isinstance(value, RainyComplexTypesTheThirteen):
            self._demo_strong_ref = value
        else:
            self._demo_strong_ref = RainyComplexTypesTheThirteen.from_alipay_dict(value)
    @property
    def demo_wink_ref(self):
        return self._demo_wink_ref

    @demo_wink_ref.setter
    def demo_wink_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourteenOne):
            self._demo_wink_ref = value
        else:
            self._demo_wink_ref = RainyComplexTypesTheFourteenOne.from_alipay_dict(value)
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, RainyComplexTypesTheThirteen):
            self._test = value
        else:
            self._test = RainyComplexTypesTheThirteen.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeSchemaapitwentythirdRainytestQueryResponse, self).parse_response_content(response_content)
        if 'demo_ref' in response:
            self.demo_ref = response['demo_ref']
        if 'demo_res' in response:
            self.demo_res = response['demo_res']
        if 'demo_strong_ref' in response:
            self.demo_strong_ref = response['demo_strong_ref']
        if 'demo_wink_ref' in response:
            self.demo_wink_ref = response['demo_wink_ref']
        if 'test' in response:
            self.test = response['test']
