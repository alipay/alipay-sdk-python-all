#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcShopCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcShopCreateResponse, self).__init__()
        self._ec_shop_id = None

    @property
    def ec_shop_id(self):
        return self._ec_shop_id

    @ec_shop_id.setter
    def ec_shop_id(self, value):
        self._ec_shop_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcShopCreateResponse, self).parse_response_content(response_content)
        if 'ec_shop_id' in response:
            self.ec_shop_id = response['ec_shop_id']
