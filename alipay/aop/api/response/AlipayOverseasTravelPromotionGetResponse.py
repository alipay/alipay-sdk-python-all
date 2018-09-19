#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromotionInfo import PromotionInfo


class AlipayOverseasTravelPromotionGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelPromotionGetResponse, self).__init__()
        self._promotions = None
        self._total = None

    @property
    def promotions(self):
        return self._promotions

    @promotions.setter
    def promotions(self, value):
        if isinstance(value, list):
            self._promotions = list()
            for i in value:
                if isinstance(i, PromotionInfo):
                    self._promotions.append(i)
                else:
                    self._promotions.append(PromotionInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelPromotionGetResponse, self).parse_response_content(response_content)
        if 'promotions' in response:
            self.promotions = response['promotions']
        if 'total' in response:
            self.total = response['total']
