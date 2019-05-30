#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSettleReceivablesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSettleReceivablesQueryResponse, self).__init__()
        self._unsettled_amount = None

    @property
    def unsettled_amount(self):
        return self._unsettled_amount

    @unsettled_amount.setter
    def unsettled_amount(self, value):
        self._unsettled_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSettleReceivablesQueryResponse, self).parse_response_content(response_content)
        if 'unsettled_amount' in response:
            self.unsettled_amount = response['unsettled_amount']
