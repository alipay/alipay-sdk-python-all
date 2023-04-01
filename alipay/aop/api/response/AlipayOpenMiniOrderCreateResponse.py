#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderCreateResponse, self).__init__()
        self._order_id = None
        self._out_order_id = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderCreateResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
