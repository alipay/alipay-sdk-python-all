#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseResourcepackageRenewConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageRenewConsultResponse, self).__init__()
        self._currency = None
        self._trade_total_amount = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def trade_total_amount(self):
        return self._trade_total_amount

    @trade_total_amount.setter
    def trade_total_amount(self, value):
        self._trade_total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageRenewConsultResponse, self).parse_response_content(response_content)
        if 'currency' in response:
            self.currency = response['currency']
        if 'trade_total_amount' in response:
            self.trade_total_amount = response['trade_total_amount']
