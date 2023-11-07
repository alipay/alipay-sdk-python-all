#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCardOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCardOrderCloseResponse, self).__init__()
        self._card_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCardOrderCloseResponse, self).parse_response_content(response_content)
        if 'card_id' in response:
            self.card_id = response['card_id']
