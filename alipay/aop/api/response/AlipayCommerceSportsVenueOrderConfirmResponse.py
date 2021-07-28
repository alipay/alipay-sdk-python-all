#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceSportsVenueOrderConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsVenueOrderConfirmResponse, self).__init__()
        self._order_id = None
        self._order_status = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsVenueOrderConfirmResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
