#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordermaterialsapplyShopCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyShopCreateResponse, self).__init__()
        self._shop_order_no = None

    @property
    def shop_order_no(self):
        return self._shop_order_no

    @shop_order_no.setter
    def shop_order_no(self, value):
        self._shop_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyShopCreateResponse, self).parse_response_content(response_content)
        if 'shop_order_no' in response:
            self.shop_order_no = response['shop_order_no']
