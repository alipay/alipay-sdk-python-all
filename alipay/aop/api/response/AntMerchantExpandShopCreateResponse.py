#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandShopCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandShopCreateResponse, self).__init__()
        self._exist_shop_id = None
        self._order_id = None

    @property
    def exist_shop_id(self):
        return self._exist_shop_id

    @exist_shop_id.setter
    def exist_shop_id(self, value):
        self._exist_shop_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandShopCreateResponse, self).parse_response_content(response_content)
        if 'exist_shop_id' in response:
            self.exist_shop_id = response['exist_shop_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
