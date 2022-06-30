#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportPromotionRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportPromotionRecommendQueryResponse, self).__init__()
        self._from_amount = None
        self._reduction_amount = None

    @property
    def from_amount(self):
        return self._from_amount

    @from_amount.setter
    def from_amount(self, value):
        self._from_amount = value
    @property
    def reduction_amount(self):
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, value):
        self._reduction_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportPromotionRecommendQueryResponse, self).parse_response_content(response_content)
        if 'from_amount' in response:
            self.from_amount = response['from_amount']
        if 'reduction_amount' in response:
            self.reduction_amount = response['reduction_amount']
