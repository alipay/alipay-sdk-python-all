#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SingleTripDurationQueryOpenapiResult import SingleTripDurationQueryOpenapiResult


class AlipayCommerceTransportIntelligentizeSingletripdurationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIntelligentizeSingletripdurationQueryResponse, self).__init__()
        self._ext_info = None
        self._result = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, SingleTripDurationQueryOpenapiResult):
                    self._result.append(i)
                else:
                    self._result.append(SingleTripDurationQueryOpenapiResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIntelligentizeSingletripdurationQueryResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'result' in response:
            self.result = response['result']
