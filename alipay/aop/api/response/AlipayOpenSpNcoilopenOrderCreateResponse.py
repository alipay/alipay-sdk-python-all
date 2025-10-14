#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNcoilopenOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNcoilopenOrderCreateResponse, self).__init__()
        self._apply_id = None
        self._order_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNcoilopenOrderCreateResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
