#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTravelRateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelRateQueryResponse, self).__init__()
        self._currency = None
        self._currency_icon = None
        self._customer_level = None
        self._rate = None
        self._rate_desc = None
        self._rate_source = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def currency_icon(self):
        return self._currency_icon

    @currency_icon.setter
    def currency_icon(self, value):
        self._currency_icon = value
    @property
    def customer_level(self):
        return self._customer_level

    @customer_level.setter
    def customer_level(self, value):
        self._customer_level = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def rate_desc(self):
        return self._rate_desc

    @rate_desc.setter
    def rate_desc(self, value):
        self._rate_desc = value
    @property
    def rate_source(self):
        return self._rate_source

    @rate_source.setter
    def rate_source(self, value):
        self._rate_source = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelRateQueryResponse, self).parse_response_content(response_content)
        if 'currency' in response:
            self.currency = response['currency']
        if 'currency_icon' in response:
            self.currency_icon = response['currency_icon']
        if 'customer_level' in response:
            self.customer_level = response['customer_level']
        if 'rate' in response:
            self.rate = response['rate']
        if 'rate_desc' in response:
            self.rate_desc = response['rate_desc']
        if 'rate_source' in response:
            self.rate_source = response['rate_source']
