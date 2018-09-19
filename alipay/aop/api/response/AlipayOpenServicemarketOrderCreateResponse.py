#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenServicemarketOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenServicemarketOrderCreateResponse, self).__init__()
        self._commodity_order_id = None
        self._mini_app_id = None

    @property
    def commodity_order_id(self):
        return self._commodity_order_id

    @commodity_order_id.setter
    def commodity_order_id(self, value):
        self._commodity_order_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenServicemarketOrderCreateResponse, self).parse_response_content(response_content)
        if 'commodity_order_id' in response:
            self.commodity_order_id = response['commodity_order_id']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
