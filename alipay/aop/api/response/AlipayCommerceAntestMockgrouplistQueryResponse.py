#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcoMockGroupInfo import EcoMockGroupInfo


class AlipayCommerceAntestMockgrouplistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAntestMockgrouplistQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, EcoMockGroupInfo):
                    self._data.append(i)
                else:
                    self._data.append(EcoMockGroupInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAntestMockgrouplistQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
