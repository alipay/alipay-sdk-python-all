#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBusinessRelationShopCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationShopCreateResponse, self).__init__()
        self._real_shop_id = None

    @property
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationShopCreateResponse, self).parse_response_content(response_content)
        if 'real_shop_id' in response:
            self.real_shop_id = response['real_shop_id']
