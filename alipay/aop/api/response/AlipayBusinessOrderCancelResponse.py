#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBusinessOrderCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessOrderCancelResponse, self).__init__()
        self._merchant_order_no = None
        self._order_no = None

    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessOrderCancelResponse, self).parse_response_content(response_content)
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
