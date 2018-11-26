#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransMergePrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransMergePrecreateResponse, self).__init__()
        self._merge_order_id = None

    @property
    def merge_order_id(self):
        return self._merge_order_id

    @merge_order_id.setter
    def merge_order_id(self, value):
        self._merge_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransMergePrecreateResponse, self).parse_response_content(response_content)
        if 'merge_order_id' in response:
            self.merge_order_id = response['merge_order_id']
