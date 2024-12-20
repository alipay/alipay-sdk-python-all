#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEbikerentalDiscountPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEbikerentalDiscountPreconsultResponse, self).__init__()
        self._discount_amount = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEbikerentalDiscountPreconsultResponse, self).parse_response_content(response_content)
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
