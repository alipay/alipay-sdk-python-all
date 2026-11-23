#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class SubAccountBalanceDTO(object):

    def __init__(self):
        self._available_amount = None
        self._balance = None
        self._freeze_amount = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._available_amount = value
        else:
            self._available_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._balance = value
        else:
            self._balance = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._freeze_amount = value
        else:
            self._freeze_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountBalanceDTO()
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'balance' in d:
            o.balance = d['balance']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        return o


