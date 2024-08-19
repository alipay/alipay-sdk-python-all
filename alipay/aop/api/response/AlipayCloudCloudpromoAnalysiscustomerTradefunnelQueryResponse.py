#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiCustomerAnalysisResult import OpenApiCustomerAnalysisResult


class AlipayCloudCloudpromoAnalysiscustomerTradefunnelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAnalysiscustomerTradefunnelQueryResponse, self).__init__()
        self._items = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, OpenApiCustomerAnalysisResult):
            self._items = value
        else:
            self._items = OpenApiCustomerAnalysisResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAnalysiscustomerTradefunnelQueryResponse, self).parse_response_content(response_content)
        if 'items' in response:
            self.items = response['items']
