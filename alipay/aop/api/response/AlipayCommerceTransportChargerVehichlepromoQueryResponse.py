#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportChargerVehichlepromoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerVehichlepromoQueryResponse, self).__init__()
        self._discount_amount = None
        self._orderStr = None
        self._vin = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerVehichlepromoQueryResponse, self).parse_response_content(response_content)
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
        if 'vin' in response:
            self.vin = response['vin']
