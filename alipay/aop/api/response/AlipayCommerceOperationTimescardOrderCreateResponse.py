#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationTimescardOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTimescardOrderCreateResponse, self).__init__()
        self._is_need_invoke_jsapi = None
        self._kabao_token = None
        self._order_id = None
        self._order_str = None

    @property
    def is_need_invoke_jsapi(self):
        return self._is_need_invoke_jsapi

    @is_need_invoke_jsapi.setter
    def is_need_invoke_jsapi(self, value):
        self._is_need_invoke_jsapi = value
    @property
    def kabao_token(self):
        return self._kabao_token

    @kabao_token.setter
    def kabao_token(self, value):
        self._kabao_token = value
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
        response = super(AlipayCommerceOperationTimescardOrderCreateResponse, self).parse_response_content(response_content)
        if 'is_need_invoke_jsapi' in response:
            self.is_need_invoke_jsapi = response['is_need_invoke_jsapi']
        if 'kabao_token' in response:
            self.kabao_token = response['kabao_token']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_str' in response:
            self.order_str = response['order_str']
