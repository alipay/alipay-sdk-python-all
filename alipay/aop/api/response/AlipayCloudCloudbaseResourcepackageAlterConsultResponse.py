#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseResourcepackageAlterConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageAlterConsultResponse, self).__init__()
        self._alter_type = None
        self._currency = None
        self._payment_direction = None
        self._trade_total_amount = None

    @property
    def alter_type(self):
        return self._alter_type

    @alter_type.setter
    def alter_type(self, value):
        self._alter_type = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def payment_direction(self):
        return self._payment_direction

    @payment_direction.setter
    def payment_direction(self, value):
        self._payment_direction = value
    @property
    def trade_total_amount(self):
        return self._trade_total_amount

    @trade_total_amount.setter
    def trade_total_amount(self, value):
        self._trade_total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageAlterConsultResponse, self).parse_response_content(response_content)
        if 'alter_type' in response:
            self.alter_type = response['alter_type']
        if 'currency' in response:
            self.currency = response['currency']
        if 'payment_direction' in response:
            self.payment_direction = response['payment_direction']
        if 'trade_total_amount' in response:
            self.trade_total_amount = response['trade_total_amount']
