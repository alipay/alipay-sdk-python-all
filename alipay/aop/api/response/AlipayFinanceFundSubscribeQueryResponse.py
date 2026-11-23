#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HudMarketItem import HudMarketItem


class AlipayFinanceFundSubscribeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceFundSubscribeQueryResponse, self).__init__()
        self._display_item = None

    @property
    def display_item(self):
        return self._display_item

    @display_item.setter
    def display_item(self, value):
        if isinstance(value, HudMarketItem):
            self._display_item = value
        else:
            self._display_item = HudMarketItem.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceFundSubscribeQueryResponse, self).parse_response_content(response_content)
        if 'display_item' in response:
            self.display_item = response['display_item']
