#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVoucherStockQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherStockQueryResponse, self).__init__()
        self._available_count = None
        self._total_count = None

    @property
    def available_count(self):
        return self._available_count

    @available_count.setter
    def available_count(self, value):
        self._available_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherStockQueryResponse, self).parse_response_content(response_content)
        if 'available_count' in response:
            self.available_count = response['available_count']
        if 'total_count' in response:
            self.total_count = response['total_count']
