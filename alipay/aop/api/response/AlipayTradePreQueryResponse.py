#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradePreQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePreQueryResponse, self).__init__()
        self._seller_type = None

    @property
    def seller_type(self):
        return self._seller_type

    @seller_type.setter
    def seller_type(self, value):
        self._seller_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePreQueryResponse, self).parse_response_content(response_content)
        if 'seller_type' in response:
            self.seller_type = response['seller_type']
