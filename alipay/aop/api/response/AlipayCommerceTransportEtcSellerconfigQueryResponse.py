#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcSellerconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcSellerconfigQueryResponse, self).__init__()
        self._query_results = None

    @property
    def query_results(self):
        return self._query_results

    @query_results.setter
    def query_results(self, value):
        self._query_results = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcSellerconfigQueryResponse, self).parse_response_content(response_content)
        if 'query_results' in response:
            self.query_results = response['query_results']
