#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantPayforprivilegePayCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegePayCreateResponse, self).__init__()
        self._order_id = None
        self._order_str = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_str(self):
        return self._order_str

    @order_str.setter
    def order_str(self, value):
        self._order_str = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegePayCreateResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_str' in response:
            self.order_str = response['order_str']
