#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCreditbankUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCreditbankUserQueryResponse, self).__init__()
        self._cb_id = None

    @property
    def cb_id(self):
        return self._cb_id

    @cb_id.setter
    def cb_id(self, value):
        self._cb_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCreditbankUserQueryResponse, self).parse_response_content(response_content)
        if 'cb_id' in response:
            self.cb_id = response['cb_id']
