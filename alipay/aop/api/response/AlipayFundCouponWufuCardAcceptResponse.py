#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCouponWufuCardAcceptResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuCardAcceptResponse, self).__init__()
        self._card_name = None
        self._card_type = None

    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuCardAcceptResponse, self).parse_response_content(response_content)
        if 'card_name' in response:
            self.card_name = response['card_name']
        if 'card_type' in response:
            self.card_type = response['card_type']
