#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleForceAmountConvertResponse(object):

    def __init__(self):
        self._amount_minor_units = None
        self._currency = None

    @property
    def amount_minor_units(self):
        return self._amount_minor_units

    @amount_minor_units.setter
    def amount_minor_units(self, value):
        self._amount_minor_units = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_minor_units:
            if hasattr(self.amount_minor_units, 'to_alipay_dict'):
                params['amount_minor_units'] = self.amount_minor_units.to_alipay_dict()
            else:
                params['amount_minor_units'] = self.amount_minor_units
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
        o = SaleForceAmountConvertResponse()
        if 'amount_minor_units' in d:
            o.amount_minor_units = d['amount_minor_units']
        if 'currency' in d:
            o.currency = d['currency']
        return o


