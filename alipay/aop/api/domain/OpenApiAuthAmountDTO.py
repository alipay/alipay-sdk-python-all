#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiAuthAmountDTO(object):

    def __init__(self):
        self._amount = None
        self._auth_factor = None
        self._currency = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def auth_factor(self):
        return self._auth_factor

    @auth_factor.setter
    def auth_factor(self, value):
        self._auth_factor = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.auth_factor:
            if hasattr(self.auth_factor, 'to_alipay_dict'):
                params['auth_factor'] = self.auth_factor.to_alipay_dict()
            else:
                params['auth_factor'] = self.auth_factor
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiAuthAmountDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'auth_factor' in d:
            o.auth_factor = d['auth_factor']
        if 'currency' in d:
            o.currency = d['currency']
        return o


