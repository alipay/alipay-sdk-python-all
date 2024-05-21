#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdJhjtestSupportauthtokenModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdJhjtestSupportauthtokenModifyResponse, self).__init__()
        self._price = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdJhjtestSupportauthtokenModifyResponse, self).parse_response_content(response_content)
        if 'price' in response:
            self.price = response['price']
