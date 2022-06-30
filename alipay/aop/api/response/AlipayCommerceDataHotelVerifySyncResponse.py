#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDataHotelVerifySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataHotelVerifySyncResponse, self).__init__()
        self._message = None
        self._shop_id = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataHotelVerifySyncResponse, self).parse_response_content(response_content)
        if 'message' in response:
            self.message = response['message']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
