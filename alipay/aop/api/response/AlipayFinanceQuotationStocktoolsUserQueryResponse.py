#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinanceQuotationStocktoolsUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceQuotationStocktoolsUserQueryResponse, self).__init__()
        self._auth_status = None
        self._expire_time = None
        self._free_experience_available = None
        self._remain_days = None
        self._suggest_price = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def free_experience_available(self):
        return self._free_experience_available

    @free_experience_available.setter
    def free_experience_available(self, value):
        self._free_experience_available = value
    @property
    def remain_days(self):
        return self._remain_days

    @remain_days.setter
    def remain_days(self, value):
        self._remain_days = value
    @property
    def suggest_price(self):
        return self._suggest_price

    @suggest_price.setter
    def suggest_price(self, value):
        self._suggest_price = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceQuotationStocktoolsUserQueryResponse, self).parse_response_content(response_content)
        if 'auth_status' in response:
            self.auth_status = response['auth_status']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'free_experience_available' in response:
            self.free_experience_available = response['free_experience_available']
        if 'remain_days' in response:
            self.remain_days = response['remain_days']
        if 'suggest_price' in response:
            self.suggest_price = response['suggest_price']
