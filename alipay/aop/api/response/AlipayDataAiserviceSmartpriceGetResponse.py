#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HelloBikePriceResultItem import HelloBikePriceResultItem


class AlipayDataAiserviceSmartpriceGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceSmartpriceGetResponse, self).__init__()
        self._promo_price_cent = None
        self._result = None

    @property
    def promo_price_cent(self):
        return self._promo_price_cent

    @promo_price_cent.setter
    def promo_price_cent(self, value):
        self._promo_price_cent = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, HelloBikePriceResultItem):
                    self._result.append(i)
                else:
                    self._result.append(HelloBikePriceResultItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceSmartpriceGetResponse, self).parse_response_content(response_content)
        if 'promo_price_cent' in response:
            self.promo_price_cent = response['promo_price_cent']
        if 'result' in response:
            self.result = response['result']
