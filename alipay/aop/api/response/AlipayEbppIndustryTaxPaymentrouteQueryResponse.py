#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryTaxPaymentrouteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryTaxPaymentrouteQueryResponse, self).__init__()
        self._pay_channel = None
        self._query_id = None

    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def query_id(self):
        return self._query_id

    @query_id.setter
    def query_id(self, value):
        self._query_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryTaxPaymentrouteQueryResponse, self).parse_response_content(response_content)
        if 'pay_channel' in response:
            self.pay_channel = response['pay_channel']
        if 'query_id' in response:
            self.query_id = response['query_id']
