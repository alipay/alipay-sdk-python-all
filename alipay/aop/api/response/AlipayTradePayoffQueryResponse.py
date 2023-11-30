#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ManjiangTestComplexOneData import ManjiangTestComplexOneData
from alipay.aop.api.domain.ResourcePackage import ResourcePackage


class AlipayTradePayoffQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePayoffQueryResponse, self).__init__()
        self._man_dddd_asaa = None
        self._sadf = None
        self._sd = None

    @property
    def man_dddd_asaa(self):
        return self._man_dddd_asaa

    @man_dddd_asaa.setter
    def man_dddd_asaa(self, value):
        if isinstance(value, ManjiangTestComplexOneData):
            self._man_dddd_asaa = value
        else:
            self._man_dddd_asaa = ManjiangTestComplexOneData.from_alipay_dict(value)
    @property
    def sadf(self):
        return self._sadf

    @sadf.setter
    def sadf(self, value):
        if isinstance(value, ResourcePackage):
            self._sadf = value
        else:
            self._sadf = ResourcePackage.from_alipay_dict(value)
    @property
    def sd(self):
        return self._sd

    @sd.setter
    def sd(self, value):
        self._sd = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePayoffQueryResponse, self).parse_response_content(response_content)
        if 'man_dddd_asaa' in response:
            self.man_dddd_asaa = response['man_dddd_asaa']
        if 'sadf' in response:
            self.sadf = response['sadf']
        if 'sd' in response:
            self.sd = response['sd']
