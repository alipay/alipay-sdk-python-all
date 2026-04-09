#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradePriceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePriceCreateResponse, self).__init__()
        self._price_id = None
        self._product_id = None

    @property
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePriceCreateResponse, self).parse_response_content(response_content)
        if 'price_id' in response:
            self.price_id = response['price_id']
        if 'product_id' in response:
            self.product_id = response['product_id']
