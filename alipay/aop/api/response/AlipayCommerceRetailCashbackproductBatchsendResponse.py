#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailCashbackproductBatchsendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailCashbackproductBatchsendResponse, self).__init__()
        self._products = None

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        if isinstance(value, list):
            self._products = list()
            for i in value:
                self._products.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailCashbackproductBatchsendResponse, self).parse_response_content(response_content)
        if 'products' in response:
            self.products = response['products']
