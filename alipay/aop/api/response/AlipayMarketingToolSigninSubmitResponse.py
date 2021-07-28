#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeOrderVO import PrizeOrderVO


class AlipayMarketingToolSigninSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolSigninSubmitResponse, self).__init__()
        self._prize_orders = None

    @property
    def prize_orders(self):
        return self._prize_orders

    @prize_orders.setter
    def prize_orders(self, value):
        if isinstance(value, list):
            self._prize_orders = list()
            for i in value:
                if isinstance(i, PrizeOrderVO):
                    self._prize_orders.append(i)
                else:
                    self._prize_orders.append(PrizeOrderVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolSigninSubmitResponse, self).parse_response_content(response_content)
        if 'prize_orders' in response:
            self.prize_orders = response['prize_orders']
