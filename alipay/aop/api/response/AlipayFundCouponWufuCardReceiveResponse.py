#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCouponWufuCardReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuCardReceiveResponse, self).__init__()
        self._card_id = None
        self._card_type = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuCardReceiveResponse, self).parse_response_content(response_content)
        if 'card_id' in response:
            self.card_id = response['card_id']
        if 'card_type' in response:
            self.card_type = response['card_type']
