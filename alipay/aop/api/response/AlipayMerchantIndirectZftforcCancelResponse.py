#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectZftforcCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectZftforcCancelResponse, self).__init__()
        self._cancel = None
        self._order_id = None

    @property
    def cancel(self):
        return self._cancel

    @cancel.setter
    def cancel(self, value):
        self._cancel = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectZftforcCancelResponse, self).parse_response_content(response_content)
        if 'cancel' in response:
            self.cancel = response['cancel']
        if 'order_id' in response:
            self.order_id = response['order_id']
