#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportIndustryProxyUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIndustryProxyUseResponse, self).__init__()
        self._industry_response = None

    @property
    def industry_response(self):
        return self._industry_response

    @industry_response.setter
    def industry_response(self, value):
        self._industry_response = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIndustryProxyUseResponse, self).parse_response_content(response_content)
        if 'industry_response' in response:
            self.industry_response = response['industry_response']
