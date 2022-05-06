#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncGfsettleprodNobillinvoiceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGfsettleprodNobillinvoiceApplyResponse, self).__init__()
        self._order_id = None
        self._process_id = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncGfsettleprodNobillinvoiceApplyResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'process_id' in response:
            self.process_id = response['process_id']
