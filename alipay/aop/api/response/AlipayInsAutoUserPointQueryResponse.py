#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoUserPointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoUserPointQueryResponse, self).__init__()
        self._can_exchange = None
        self._can_exchange_amount = None
        self._can_save_amount = None
        self._can_use_amount = None
        self._recommend_exchange = None
        self._total_limit = None
        self._total_save_amount = None

    @property
    def can_exchange(self):
        return self._can_exchange

    @can_exchange.setter
    def can_exchange(self, value):
        self._can_exchange = value
    @property
    def can_exchange_amount(self):
        return self._can_exchange_amount

    @can_exchange_amount.setter
    def can_exchange_amount(self, value):
        self._can_exchange_amount = value
    @property
    def can_save_amount(self):
        return self._can_save_amount

    @can_save_amount.setter
    def can_save_amount(self, value):
        self._can_save_amount = value
    @property
    def can_use_amount(self):
        return self._can_use_amount

    @can_use_amount.setter
    def can_use_amount(self, value):
        self._can_use_amount = value
    @property
    def recommend_exchange(self):
        return self._recommend_exchange

    @recommend_exchange.setter
    def recommend_exchange(self, value):
        self._recommend_exchange = value
    @property
    def total_limit(self):
        return self._total_limit

    @total_limit.setter
    def total_limit(self, value):
        self._total_limit = value
    @property
    def total_save_amount(self):
        return self._total_save_amount

    @total_save_amount.setter
    def total_save_amount(self, value):
        self._total_save_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoUserPointQueryResponse, self).parse_response_content(response_content)
        if 'can_exchange' in response:
            self.can_exchange = response['can_exchange']
        if 'can_exchange_amount' in response:
            self.can_exchange_amount = response['can_exchange_amount']
        if 'can_save_amount' in response:
            self.can_save_amount = response['can_save_amount']
        if 'can_use_amount' in response:
            self.can_use_amount = response['can_use_amount']
        if 'recommend_exchange' in response:
            self.recommend_exchange = response['recommend_exchange']
        if 'total_limit' in response:
            self.total_limit = response['total_limit']
        if 'total_save_amount' in response:
            self.total_save_amount = response['total_save_amount']
