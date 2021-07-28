#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantOrderCreateandpayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantOrderCreateandpayResponse, self).__init__()
        self._order_id = None
        self._payment_status = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def payment_status(self):
        return self._payment_status

    @payment_status.setter
    def payment_status(self, value):
        self._payment_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantOrderCreateandpayResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'payment_status' in response:
            self.payment_status = response['payment_status']
