#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneCommonPreOrderResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommonPreOrderResponse, self).__init__()
        self._pre_order_id = None
        self._product_plan_id = None

    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommonPreOrderResponse, self).parse_response_content(response_content)
        if 'pre_order_id' in response:
            self.pre_order_id = response['pre_order_id']
        if 'product_plan_id' in response:
            self.product_plan_id = response['product_plan_id']
