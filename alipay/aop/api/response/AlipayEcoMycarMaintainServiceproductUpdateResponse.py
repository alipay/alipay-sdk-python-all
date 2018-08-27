#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarMaintainServiceproductUpdateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarMaintainServiceproductUpdateResponse, self).__init__()
        self._product_id = None

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarMaintainServiceproductUpdateResponse, self).parse_response_content(response_content)
        if 'product_id' in response:
            self.product_id = response['product_id']
