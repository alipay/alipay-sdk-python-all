#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseResourcepackageItempackageConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageItempackageConsultResponse, self).__init__()
        self._original_total_amount = None
        self._original_unit_amount = None
        self._trade_total_amount = None

    @property
    def original_total_amount(self):
        return self._original_total_amount

    @original_total_amount.setter
    def original_total_amount(self, value):
        self._original_total_amount = value
    @property
    def original_unit_amount(self):
        return self._original_unit_amount

    @original_unit_amount.setter
    def original_unit_amount(self, value):
        self._original_unit_amount = value
    @property
    def trade_total_amount(self):
        return self._trade_total_amount

    @trade_total_amount.setter
    def trade_total_amount(self, value):
        self._trade_total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageItempackageConsultResponse, self).parse_response_content(response_content)
        if 'original_total_amount' in response:
            self.original_total_amount = response['original_total_amount']
        if 'original_unit_amount' in response:
            self.original_unit_amount = response['original_unit_amount']
        if 'trade_total_amount' in response:
            self.trade_total_amount = response['trade_total_amount']
