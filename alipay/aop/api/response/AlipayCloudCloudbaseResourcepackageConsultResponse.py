#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseResourcepackageConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageConsultResponse, self).__init__()
        self._concurrency = None
        self._original_price = None
        self._trade_price = None

    @property
    def concurrency(self):
        return self._concurrency

    @concurrency.setter
    def concurrency(self, value):
        self._concurrency = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def trade_price(self):
        return self._trade_price

    @trade_price.setter
    def trade_price(self, value):
        self._trade_price = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageConsultResponse, self).parse_response_content(response_content)
        if 'concurrency' in response:
            self.concurrency = response['concurrency']
        if 'original_price' in response:
            self.original_price = response['original_price']
        if 'trade_price' in response:
            self.trade_price = response['trade_price']
