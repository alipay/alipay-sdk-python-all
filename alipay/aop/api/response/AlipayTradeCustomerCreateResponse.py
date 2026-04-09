#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCustomerCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCustomerCreateResponse, self).__init__()
        self._customer_id = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCustomerCreateResponse, self).parse_response_content(response_content)
        if 'customer_id' in response:
            self.customer_id = response['customer_id']
