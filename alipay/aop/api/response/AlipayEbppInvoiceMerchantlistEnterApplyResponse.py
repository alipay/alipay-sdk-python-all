#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceMerchantlistEnterApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceMerchantlistEnterApplyResponse, self).__init__()
        self._process_id = None

    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceMerchantlistEnterApplyResponse, self).parse_response_content(response_content)
        if 'process_id' in response:
            self.process_id = response['process_id']
