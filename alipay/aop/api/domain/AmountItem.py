#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmountItem(object):

    def __init__(self):
        self._balance_amount = None
        self._currency = None
        self._frozen_balance_amount = None

    @property
    def balance_amount(self):
        return self._balance_amount

    @balance_amount.setter
    def balance_amount(self, value):
        self._balance_amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def frozen_balance_amount(self):
        return self._frozen_balance_amount

    @frozen_balance_amount.setter
    def frozen_balance_amount(self, value):
        self._frozen_balance_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance_amount:
            if hasattr(self.balance_amount, 'to_alipay_dict'):
                params['balance_amount'] = self.balance_amount.to_alipay_dict()
            else:
                params['balance_amount'] = self.balance_amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.frozen_balance_amount:
            if hasattr(self.frozen_balance_amount, 'to_alipay_dict'):
                params['frozen_balance_amount'] = self.frozen_balance_amount.to_alipay_dict()
            else:
                params['frozen_balance_amount'] = self.frozen_balance_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmountItem()
        if 'balance_amount' in d:
            o.balance_amount = d['balance_amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'frozen_balance_amount' in d:
            o.frozen_balance_amount = d['frozen_balance_amount']
        return o


