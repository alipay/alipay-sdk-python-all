#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransRenderPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransRenderPayResponse, self).__init__()
        self._biz_scene = None
        self._initialize_code = None
        self._initialize_code_type = None
        self._order_id = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def initialize_code(self):
        return self._initialize_code

    @initialize_code.setter
    def initialize_code(self, value):
        self._initialize_code = value
    @property
    def initialize_code_type(self):
        return self._initialize_code_type

    @initialize_code_type.setter
    def initialize_code_type(self, value):
        self._initialize_code_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransRenderPayResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'initialize_code' in response:
            self.initialize_code = response['initialize_code']
        if 'initialize_code_type' in response:
            self.initialize_code_type = response['initialize_code_type']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'product_code' in response:
            self.product_code = response['product_code']
