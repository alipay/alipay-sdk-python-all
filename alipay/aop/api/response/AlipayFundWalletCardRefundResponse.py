#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletCardRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletCardRefundResponse, self).__init__()
        self._product_code = None
        self._total_amount = None

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletCardRefundResponse, self).parse_response_content(response_content)
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
