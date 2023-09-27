#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendPrice import RecommendPrice


class AlipayDataIotdataIdpsolutionProductpriceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataIotdataIdpsolutionProductpriceQueryResponse, self).__init__()
        self._price_dist = None
        self._suggest_price = None

    @property
    def price_dist(self):
        return self._price_dist

    @price_dist.setter
    def price_dist(self, value):
        if isinstance(value, list):
            self._price_dist = list()
            for i in value:
                if isinstance(i, RecommendPrice):
                    self._price_dist.append(i)
                else:
                    self._price_dist.append(RecommendPrice.from_alipay_dict(i))
    @property
    def suggest_price(self):
        return self._suggest_price

    @suggest_price.setter
    def suggest_price(self, value):
        self._suggest_price = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataIotdataIdpsolutionProductpriceQueryResponse, self).parse_response_content(response_content)
        if 'price_dist' in response:
            self.price_dist = response['price_dist']
        if 'suggest_price' in response:
            self.suggest_price = response['suggest_price']
