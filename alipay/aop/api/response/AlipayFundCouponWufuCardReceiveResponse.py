#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCouponWufuCardReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuCardReceiveResponse, self).__init__()
        self._card_type = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuCardReceiveResponse, self).parse_response_content(response_content)
        if 'card_type' in response:
            self.card_type = response['card_type']
