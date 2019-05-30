#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsNanjingtestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsNanjingtestQueryResponse, self).__init__()
        self._total_results = None

    @property
    def total_results(self):
        return self._total_results

    @total_results.setter
    def total_results(self, value):
        self._total_results = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsNanjingtestQueryResponse, self).parse_response_content(response_content)
        if 'total_results' in response:
            self.total_results = response['total_results']
