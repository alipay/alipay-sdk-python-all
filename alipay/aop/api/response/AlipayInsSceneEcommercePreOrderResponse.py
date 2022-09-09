#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneEcommercePreOrderResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommercePreOrderResponse, self).__init__()
        self._pre_order_id = None

    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommercePreOrderResponse, self).parse_response_content(response_content)
        if 'pre_order_id' in response:
            self.pre_order_id = response['pre_order_id']
