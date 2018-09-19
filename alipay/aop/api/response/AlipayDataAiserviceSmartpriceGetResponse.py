#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataAiserviceSmartpriceGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceSmartpriceGetResponse, self).__init__()
        self._promo_price_cent = None

    @property
    def promo_price_cent(self):
        return self._promo_price_cent

    @promo_price_cent.setter
    def promo_price_cent(self, value):
        self._promo_price_cent = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceSmartpriceGetResponse, self).parse_response_content(response_content)
        if 'promo_price_cent' in response:
            self.promo_price_cent = response['promo_price_cent']
