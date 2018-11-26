#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeInfo import PrizeInfo


class AlipayOverseasTravelGkaCampprizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelGkaCampprizeQueryResponse, self).__init__()
        self._prizes = None

    @property
    def prizes(self):
        return self._prizes

    @prizes.setter
    def prizes(self, value):
        if isinstance(value, list):
            self._prizes = list()
            for i in value:
                if isinstance(i, PrizeInfo):
                    self._prizes.append(i)
                else:
                    self._prizes.append(PrizeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelGkaCampprizeQueryResponse, self).parse_response_content(response_content)
        if 'prizes' in response:
            self.prizes = response['prizes']
