#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsProduct import InsProduct


class AlipayInsCooperationProductQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsCooperationProductQueryResponse, self).__init__()
        self._product = None

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, InsProduct):
            self._product = value
        else:
            self._product = InsProduct.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsCooperationProductQueryResponse, self).parse_response_content(response_content)
        if 'product' in response:
            self.product = response['product']
