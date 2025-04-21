#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineSmddShopJoinNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddShopJoinNotifyResponse, self).__init__()
        self._shop_id = None

    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddShopJoinNotifyResponse, self).parse_response_content(response_content)
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
