#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpBusinessIndicator import EpBusinessIndicator


class ZhimaCreditEpBusinessIndicatorQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpBusinessIndicatorQueryResponse, self).__init__()
        self._array_data = None
        self._business_key = None

    @property
    def array_data(self):
        return self._array_data

    @array_data.setter
    def array_data(self, value):
        if isinstance(value, list):
            self._array_data = list()
            for i in value:
                if isinstance(i, EpBusinessIndicator):
                    self._array_data.append(i)
                else:
                    self._array_data.append(EpBusinessIndicator.from_alipay_dict(i))
    @property
    def business_key(self):
        return self._business_key

    @business_key.setter
    def business_key(self, value):
        self._business_key = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpBusinessIndicatorQueryResponse, self).parse_response_content(response_content)
        if 'array_data' in response:
            self.array_data = response['array_data']
        if 'business_key' in response:
            self.business_key = response['business_key']
