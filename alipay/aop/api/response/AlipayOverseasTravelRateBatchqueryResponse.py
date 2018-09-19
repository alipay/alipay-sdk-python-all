#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTravelRateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelRateBatchqueryResponse, self).__init__()
        self._rate_desc = None
        self._rate_source = None
        self._rates = None

    @property
    def rate_desc(self):
        return self._rate_desc

    @rate_desc.setter
    def rate_desc(self, value):
        self._rate_desc = value
    @property
    def rate_source(self):
        return self._rate_source

    @rate_source.setter
    def rate_source(self, value):
        self._rate_source = value
    @property
    def rates(self):
        return self._rates

    @rates.setter
    def rates(self, value):
        self._rates = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelRateBatchqueryResponse, self).parse_response_content(response_content)
        if 'rate_desc' in response:
            self.rate_desc = response['rate_desc']
        if 'rate_source' in response:
            self.rate_source = response['rate_source']
        if 'rates' in response:
            self.rates = response['rates']
