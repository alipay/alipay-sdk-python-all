#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoLogisticsExpressPriceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoLogisticsExpressPriceQueryResponse, self).__init__()
        self._extra_weight_price = None
        self._extra_weight_unit = None
        self._preset_weight = None
        self._preset_weight_price = None

    @property
    def extra_weight_price(self):
        return self._extra_weight_price

    @extra_weight_price.setter
    def extra_weight_price(self, value):
        self._extra_weight_price = value
    @property
    def extra_weight_unit(self):
        return self._extra_weight_unit

    @extra_weight_unit.setter
    def extra_weight_unit(self, value):
        self._extra_weight_unit = value
    @property
    def preset_weight(self):
        return self._preset_weight

    @preset_weight.setter
    def preset_weight(self, value):
        self._preset_weight = value
    @property
    def preset_weight_price(self):
        return self._preset_weight_price

    @preset_weight_price.setter
    def preset_weight_price(self, value):
        self._preset_weight_price = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoLogisticsExpressPriceQueryResponse, self).parse_response_content(response_content)
        if 'extra_weight_price' in response:
            self.extra_weight_price = response['extra_weight_price']
        if 'extra_weight_unit' in response:
            self.extra_weight_unit = response['extra_weight_unit']
        if 'preset_weight' in response:
            self.preset_weight = response['preset_weight']
        if 'preset_weight_price' in response:
            self.preset_weight_price = response['preset_weight_price']
