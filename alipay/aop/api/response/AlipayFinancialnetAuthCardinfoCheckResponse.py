#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthCardinfoCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthCardinfoCheckResponse, self).__init__()
        self._bank = None
        self._cache_key = None
        self._card_type = None
        self._validated = None

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        self._bank = value
    @property
    def cache_key(self):
        return self._cache_key

    @cache_key.setter
    def cache_key(self, value):
        self._cache_key = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def validated(self):
        return self._validated

    @validated.setter
    def validated(self, value):
        self._validated = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthCardinfoCheckResponse, self).parse_response_content(response_content)
        if 'bank' in response:
            self.bank = response['bank']
        if 'cache_key' in response:
            self.cache_key = response['cache_key']
        if 'card_type' in response:
            self.card_type = response['card_type']
        if 'validated' in response:
            self.validated = response['validated']
