#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdOrderCreateResponse, self).__init__()
        self._order_id = None
        self._order_outer_id = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_outer_id(self):
        return self._order_outer_id

    @order_outer_id.setter
    def order_outer_id(self, value):
        self._order_outer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdOrderCreateResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_outer_id' in response:
            self.order_outer_id = response['order_outer_id']
