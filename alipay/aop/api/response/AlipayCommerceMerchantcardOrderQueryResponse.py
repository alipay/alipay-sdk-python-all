#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardOrderInfo import CardOrderInfo


class AlipayCommerceMerchantcardOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardOrderQueryResponse, self).__init__()
        self._card_order_info = None

    @property
    def card_order_info(self):
        return self._card_order_info

    @card_order_info.setter
    def card_order_info(self, value):
        if isinstance(value, CardOrderInfo):
            self._card_order_info = value
        else:
            self._card_order_info = CardOrderInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardOrderQueryResponse, self).parse_response_content(response_content)
        if 'card_order_info' in response:
            self.card_order_info = response['card_order_info']
