#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataTradeHabbitQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataTradeHabbitQueryResponse, self).__init__()
        self._trade_habit_info = None

    @property
    def trade_habit_info(self):
        return self._trade_habit_info

    @trade_habit_info.setter
    def trade_habit_info(self, value):
        self._trade_habit_info = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataTradeHabbitQueryResponse, self).parse_response_content(response_content)
        if 'trade_habit_info' in response:
            self.trade_habit_info = response['trade_habit_info']
