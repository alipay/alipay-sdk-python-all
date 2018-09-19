#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTransferThirdpartyBillCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTransferThirdpartyBillCreateResponse, self).__init__()
        self._order_id = None
        self._order_type = None
        self._payment_id = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTransferThirdpartyBillCreateResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'payment_id' in response:
            self.payment_id = response['payment_id']
