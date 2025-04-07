#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtravelHotelSupplyPriceDTO(object):

    def __init__(self):
        self._amount = None
        self._currency_code = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtravelHotelSupplyPriceDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        return o


