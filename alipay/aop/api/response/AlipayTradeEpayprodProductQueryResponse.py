#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeEpayprodProductQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeEpayprodProductQueryResponse, self).__init__()
        self._product_open_status = None

    @property
    def product_open_status(self):
        return self._product_open_status

    @product_open_status.setter
    def product_open_status(self, value):
        self._product_open_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeEpayprodProductQueryResponse, self).parse_response_content(response_content)
        if 'product_open_status' in response:
            self.product_open_status = response['product_open_status']
