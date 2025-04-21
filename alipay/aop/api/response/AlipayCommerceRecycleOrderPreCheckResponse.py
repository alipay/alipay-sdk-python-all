#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleOrderPreCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrderPreCheckResponse, self).__init__()
        self._order_status = None
        self._order_status_reason = None

    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_status_reason(self):
        return self._order_status_reason

    @order_status_reason.setter
    def order_status_reason(self, value):
        self._order_status_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrderPreCheckResponse, self).parse_response_content(response_content)
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_status_reason' in response:
            self.order_status_reason = response['order_status_reason']
