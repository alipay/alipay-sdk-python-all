#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVoucherStockCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherStockCreateResponse, self).__init__()
        self._duplicate_count = None
        self._fail_count = None
        self._stock_id = None
        self._success_count = None

    @property
    def duplicate_count(self):
        return self._duplicate_count

    @duplicate_count.setter
    def duplicate_count(self, value):
        self._duplicate_count = value
    @property
    def fail_count(self):
        return self._fail_count

    @fail_count.setter
    def fail_count(self, value):
        self._fail_count = value
    @property
    def stock_id(self):
        return self._stock_id

    @stock_id.setter
    def stock_id(self, value):
        self._stock_id = value
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherStockCreateResponse, self).parse_response_content(response_content)
        if 'duplicate_count' in response:
            self.duplicate_count = response['duplicate_count']
        if 'fail_count' in response:
            self.fail_count = response['fail_count']
        if 'stock_id' in response:
            self.stock_id = response['stock_id']
        if 'success_count' in response:
            self.success_count = response['success_count']
