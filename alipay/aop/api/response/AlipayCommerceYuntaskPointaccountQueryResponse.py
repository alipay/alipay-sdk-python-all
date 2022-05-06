#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskPointaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskPointaccountQueryResponse, self).__init__()
        self._available_amount = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskPointaccountQueryResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
