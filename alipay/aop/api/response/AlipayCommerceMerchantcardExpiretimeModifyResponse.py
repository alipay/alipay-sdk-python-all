#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardExpiretimeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardExpiretimeModifyResponse, self).__init__()
        self._card_expand_order_id = None

    @property
    def card_expand_order_id(self):
        return self._card_expand_order_id

    @card_expand_order_id.setter
    def card_expand_order_id(self, value):
        self._card_expand_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardExpiretimeModifyResponse, self).parse_response_content(response_content)
        if 'card_expand_order_id' in response:
            self.card_expand_order_id = response['card_expand_order_id']
