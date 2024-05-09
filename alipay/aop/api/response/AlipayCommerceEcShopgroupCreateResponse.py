#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcShopgroupCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcShopgroupCreateResponse, self).__init__()
        self._shop_cnt = None
        self._shop_group_id = None

    @property
    def shop_cnt(self):
        return self._shop_cnt

    @shop_cnt.setter
    def shop_cnt(self, value):
        self._shop_cnt = value
    @property
    def shop_group_id(self):
        return self._shop_group_id

    @shop_group_id.setter
    def shop_group_id(self, value):
        self._shop_group_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcShopgroupCreateResponse, self).parse_response_content(response_content)
        if 'shop_cnt' in response:
            self.shop_cnt = response['shop_cnt']
        if 'shop_group_id' in response:
            self.shop_group_id = response['shop_group_id']
